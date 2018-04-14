import os
import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
#static_dir = os.path.join(os.path.dirname(__file__), 'static')

jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)
#css_url = url_for('static', filename='static/styles.css')

def render_str(template, **params):
	t = jinja_env.get_template(template)
	return t.render(params)

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render(self, template, **kw):
		self.write(render_str(template, **kw))

class Rot13(Handler):
    def get(self):
        self.render("rot13.html", text='hello')

    def post(self):
    	text_shift = ''
    	text = self.request.get('text')
    	if text:
    		text_shift = text.encode('rot13')
    	self.render('rot13.html', text=text_shift)


app = webapp2.WSGIApplication([
    ('/', Rot13)], debug=True)
