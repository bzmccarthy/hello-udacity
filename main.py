
import webapp2

form = '''
<form method='post'> 
	What is your birthday?
	<br>
	<label> Month
		<input type='text' name='month'>
	</label>
	<label> Day
		<input type='text' name='day'>
	</label>
	<label> Year
		<input type='text' name='year'>
	</label>
	<br>
	<br>
	<input type="submit">
</form>
'''

class MainPage(webapp2.RequestHandler):
    
    def get(self):
    	self.response.headers['Content-Type'] = 'text/html'
        self.response.write(form)

    def post(self):
    	self.response.write("Thanks! That's a totaly valid day!")

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
