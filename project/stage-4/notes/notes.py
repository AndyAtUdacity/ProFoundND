import os
import cgi
import urllib
from google.appengine.ext	import ndb
from content import COURSES, THINKING, TOPICS, SECTIONS
import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__))
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, courses=COURSES, sections=SECTIONS, **kw))

class MainPage(Handler):
	def get(self):
		self.render("main_page.html", page_name="home")

class NanodegreeHandler(Handler):
	def get(self):
		self.render('nanodegree_notes.html', page_name="notes")

class CourseHandler(Handler):
	def get(self, course_number):
		self.render("course.html", course_number=int(course_number), course=COURSES[int(course_number)-1], page_name="notes")

class LessonHandler(Handler):
	def get(self, course_number, lesson_number):
		self.render("lesson.html", lesson_number=int(lesson_number), lesson=COURSES[int(course_number)-1]['lessons'][int(lesson_number)-1], page_name="notes")

class SubmissionListHandler(Handler):
	def get(self):
		guestbook_name = self.request.get('guestbook_name', DEFAULT_GUESTBOOK_NAME)
		submissions_query = Submission.query(
			ancestor=guestbook_key(guestbook_name)).order(-Submission.date)
		submissions = submissions_query.fetch(10)
		self.render('guestbook.html', submissions=submissions, page_name="submissions")

class SubmissionHandler(Handler):
	def get(self):
		self.render('add_submission.html', page_name="submissions" )
	def post(self):
		guestbook_name = self.request.get('guestbook_name', DEFAULT_GUESTBOOK_NAME)
		submission = Submission(parent=guestbook_key(guestbook_name))
		submission.name = self.request.get('name')
		submission.link = self.request.get('link')
		submission.description = self.request.get('description')
		submission.image_url = self.request.get('image_url')
		submission.put()
		# query_params = {'guestbook_name' : guestbook_name}
		self.redirect('/student_submissions/') # + urllib.urlencode(query_params))

class ThinkingHandler(Handler):
	def get(self):
		self.render('thinking_like_a_programmer.html', ways_of_thinking=THINKING, page_name="thinking")

class ResourcesHandler(Handler):
	def get(self):
		self.render('additional_resources.html', topics=TOPICS, page_name="resources")

DEFAULT_GUESTBOOK_NAME = 'default_guestbook'
def guestbook_key(guestbook_name=DEFAULT_GUESTBOOK_NAME):
	return ndb.Key('Guestbook', guestbook_name)

class Submission(ndb.Model):
  """A main model for representing an individual Guestbook entry."""
  # author = ndb.StructuredProperty(Author)
  link = ndb.StringProperty(indexed=False)
  description = ndb.StringProperty(indexed=False)
  date = ndb.DateTimeProperty(auto_now_add=True)
  image_url = ndb.StringProperty(indexed=False)
  name = ndb.StringProperty(indexed=False)

application = webapp2.WSGIApplication([
	('/additional_resources/', ResourcesHandler),
	('/nanodegree_notes/', NanodegreeHandler),
	('/thinking_like_a_programmer/', ThinkingHandler),
  (r'/nanodegree_notes/course/(\d+)/', CourseHandler),
  (r'/nanodegree_notes/course/(\d+)/lesson/(\d+)/', LessonHandler),
  ('/student_submissions/add', SubmissionHandler),
  ('/student_submissions/', SubmissionListHandler),
  ('/*', MainPage)
], debug=True)



