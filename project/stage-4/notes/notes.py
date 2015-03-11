import os
import urllib

from google.appengine.api import users
from google.appengine.ext	import ndb

from content import COURSES

import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

# JINJA_ENVIRONMENT = jinja2.Environment(
#   loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
#   extensions=['jinja2.ext.autoescape'],
#   autoescape=True)



class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class MainPage(Handler):
  def get(self):
    self.render("index.html", courses=COURSES)

class CourseHandler(Handler):
	def get(self, course_number):
		self.render("course.html", course_number=int(course_number)+1, course=COURSES[int(course_number)])

class LessonHandler(Handler):
	def get(self, course_number, lesson_number):
		self.render("lesson.html", lesson_number=int(lesson_number)+1, lesson=COURSES[int(course_number)]['lessons'][int(lesson_number)])

application = webapp2.WSGIApplication([
	('/notes/', MainPage),
  (r'/notes/course/(\d+)/', CourseHandler),
  (r'/notes/course/(\d+)/lesson/(\d+)/', LessonHandler),
  ('/*', MainPage)
], debug=True)



