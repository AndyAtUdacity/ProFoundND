import webapp2
import string

# The FORM variable contains an HTML form with three text entry boxes
# which a user can enter their birthday into. These text inputs
# contain a value attribute with new Python syntax. You'll learn about
# this in the section in this lesson on String Substitution
FORM = """
<form method="post">
	What is your birthday?
	<br>

	<label> Month
		<input type="text" name="m" value="%(m)s">
	</label>

	<label> Day
		<input type="text" name="d" value="%(d)s">
	</label>

	<label> Year
		<input type="text" name="y" value="%(y)s">
	</label>

	<div style="color: red">%(error)s</div>

	<br>
	<br>
	<input type="submit">
</form>
"""
class MainPage(webapp2.RequestHandler):

	# Steve walks you through this function in the video called "Substituting Into Our Form"
	def write_form(self, error_text="", month_entered="", day_entered="", year_entered=""):
		# There's a lot of new syntax in this next bit of code.
		# You'll learn how this code actually substitues text into the 'value'
		# attributes of the FORM you see above.
		self.response.out.write(FORM % {"error" : error_text,
																		"m" : escape_html(month_entered), # the escape_html function is near the bottom of this file
																		"d"   : escape_html(day_entered),
																		"y"  : escape_html(year_entered)})
	def get(self):
		self.write_form()

	def post(self):
		# These three lines store the user's birthday input data as variables
		# (like user_month) which we can then manipulate later.
		user_month = self.request.get('m')
		user_day   = self.request.get('d')
		user_year  = self.request.get('y')

		# The valid_month, valid_day, and valid_year functions are defined
		# at the bottom of this file.
		month = valid_month(user_month)
		day   = valid_day(user_day)
		year  = valid_year(user_year)

		if not (month and day and year):
			self.write_form("That doesn't look like a valid date!",
				user_month, user_day, user_year)

		# The line of code in the else block performs a "redirect" to a
		# different URL when the user enters a valid date.
		else:
			self.redirect("/thanks")

# When the user is sent to the /thanks URL, this is the Hanlder
# that handles the request.
class ThanksHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write("Thanks! That's a totally valid day!")

# This is the code that specifies that the /thanks URL should be
# handled by ThanksHandler
app = webapp2.WSGIApplication([('/', MainPage),
															 ('/thanks', ThanksHandler)
															], debug=True)

# You'll learn more about what's called "HTML escaping"
# in this lesson.
def escape_html(s):
  s = s.replace('&', '&amp;')
  s = s.replace('>', '&gt;')
  s = s.replace('<', '&lt;')
  s = s.replace('"', '&quot;')
  return s

def valid_month(month):
	valid_months = ['Jan','Feb','Mar','Apr','May','Jun',
									'Jul','Aug','Sep','Oct','Nov','Dec']
	# the following 3 lines of code convert input like 'feBruAry' to 'Feb'
	lower_case_month = month.lower()
	first_letter_cap_month = lower_case_month.capitalize()
	short_month = first_letter_cap_month[:3]
	# the following code returns the properly-capitalized input IF it's a real month
	if short_month in valid_months:
		return first_letter_cap_month
	else:
		return None

def valid_day(day):
	# these two lines prevent an error that would occur if the user didn't enter anything (empty string).
	if day == "":
		return None

	# This line ensures that day is a number, not a string.
	day_as_num = int(day)

	# The following code ensures that the day is between 1 and 31.
	if (day_as_num >= 1) and (day_as_num <= 31):
		return day_as_num
	else:
		return None

def valid_year(year):
	if year == "":
		return None
	year = int(year)
	if (year >= 1900) and (year <= 2020):
		return year
	else:
		return None
