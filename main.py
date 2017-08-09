#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from google.appengine.ext import ndb
import logging
import jinja2
import os

jinja_environment = jinja2.Environment(
   loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
#
#add_item_from = 
#<form action = "store_item" method = "post">
#    Name: <input type = "text" name = "item_name"/><br>
#    Quanity: <input type = "number" name = "item_quantity" min = 1/> <br>
#    <input type = "submit"/>
#
#</form>




class storeItemHandler(webapp2.RequestHandler):
    def post(self):
        item_name = self.request.get('item_name')
        item_quantity = int(self.request.get('item_quantity'))

        existing_item_query = ShoppingItem.query(ShoppingItem. name == item_name)
        existing_item = existing_item_query.get()
        if existing_item is not None:
            if item_quantity == 0:
                existing_item.key.delete()
            else:

                existing_item.quantity += item_quantity
                existing_item.put()
        else:
            if item_quantity > 0:
                item = ShoppingItem(name = item_name, quantity = item_quantity)
                key = item.put()
                logging.info('The key for the item %s is %s' % (item,key))
        self.redirect('/')

class AddItemHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(add_item_from)


class ShoppingItem(ndb.Model):
    name = ndb.StringProperty(required = True)
    quantity = ndb.IntegerProperty(required = True)

class Home(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/home.html')
        items_query = ShoppingItem.query()
        items = items_query.fetch()
        self.response.write('<ul>')
        for item in items:
            self.response.write('<li>%s (%d) </li>' % (item.name, item.quantity))
            self.response.write('</ul>')
            self.response.write('<a href = "/add_item"> Add Items</a>')
        self.response.out.write(template.render())

class Profile(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/profile.html')
        items_query = ShoppingItem.query()
        items = items_query.fetch()
        self.response.write('<ul>')
        for item in items:
            self.response.write('<li>%s (%d) </li>' % (item.name, item.quantity))
            self.response.write('</ul>')
            self.response.write('<a href = "/add_item"> Add Items</a>')
        self.response.out.write(template.render())
class Basketball(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('template/basketball.html')
        self.response.out.write(template.render())
class Basketweaving(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('template/basketeaving.html')
        self.response.out.write(template.render())
class Baseball(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('template/baseball.html')
        self.response.out.write(template.render())
app = webapp2.WSGIApplication([
    ('/', Home),
    ('/profile', Profile),
    ('/basketball', Basketball),
    ('/basketweaving', Basketweaving),
    ('/add_item', AddItemHandler),
    ('/store_item',storeItemHandler)

], debug=True)
