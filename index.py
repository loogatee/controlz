
import logging
import cgi
import datetime
import wsgiref.handlers
import string
import urllib2
import subprocess
import re
import os
import sys




from jinja2 import Environment, FileSystemLoader, TemplateNotFound
from jinja2.defaults import DEFAULT_NAMESPACE


from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import memcache
from google.appengine.api import images


template_dir      = os.path.join(os.path.dirname(__file__),'templates')
#jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape = True)

jinja_environment = Environment(loader=FileSystemLoader(template_dir), autoescape = True)



#
#  Index Page:  comes completely from the template
#
#mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
class Index_Page(webapp.RequestHandler):
  def get(self):

    template = jinja_environment.get_template('index.html')
    fdata    = template.render()

    self.response.headers['Content-Type'] = 'text/html'
    self.response.out.write(fdata)

#
#
#
#mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
def main():
  logging.getLogger().setLevel(logging.DEBUG)
  application = webapp.WSGIApplication(

       [
         ('/',     Index_Page),                  # 
       ],
       debug=True)

  wsgiref.handlers.CGIHandler().run(application)


#
#
#mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
if __name__ == "__main__":
  main()

