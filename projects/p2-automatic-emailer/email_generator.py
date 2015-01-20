import os

def generate_email_text(name, company, position):
	greeting = "Dear " + name + ','
	introduction = "I saw that " + company + \
	" is looking to hire a " + position + " and I think I may be the perfect fit."
	body = "I've attached my resume to this email. Please take a look."
	signature = """Sincerely,

Andy Brown"""
	return greeting + '\n\n' + introduction + '\n\n' + body + '\n\n' + signature

# print make_email('Chris', 'Udacity', 'Course Developer')

def make_file_from_email_text(email_text, new_file_name):
	new_email_file = open(new_file_name, 'w') # the 'w' means we are 'w'riting a new file.
	new_email_file.write(email_text)
	new_email_file.close()

def make_email_file(name, company, position):
	email_text = generate_email_text(name, company, position)
	file_name = company + '_' + position + '.txt'
	make_file_from_email_text(email_text, file_name)

def generate_email_html(name, company, position):
	email_html = """
	<div id="greeting">
		<p>Dear %s,</p>
	</div>
	<div id="main-text">
		<p>I saw that %s is looking to hire a %s and I think I may be the perfect fit.</p>
		<p>I've attached my resume to this email. Please take a look.</p>
	</div>
	<div id="signature">
		<p>Sincerely,</p>
		<p>Andy Brown</p>
	</div>
	""" % (name, company, position)
	return email_html

make_email_file('Chris', 'Udacity', 'Course Developer', '')