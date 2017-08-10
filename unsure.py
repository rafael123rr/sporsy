import webapp2
from google.appengine.ext import ndb
import logging
import jinja2
import os

jinja_environment = jinja2.Environment(
   loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/profile.html')

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/home.html')
        self.response.out.write(template.render())

class ShoppingItem(ndb.Model):
    name = ndb.StringProperty(required = True)
    age = ndb.IntegerProperty(required = True)
    birthday = ndb.IntegerProperty(required = True)
    name = ndb.StringProperty(required = True)

class AddItemHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(add_item_from)

class ProfileHandler(webapp2.RequestHandler):
    def post(self):
        name = self.request
