
import webapp2
from google.appengine.ext import ndb
import logging
import jinja2
import os

jinja_environment = jinja2.Environment(
   loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


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
        self.response.write(add_item_form)

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

class ShoppingItem(ndb.Model):
    name = ndb.StringProperty(required = True)
    quantity = ndb.IntegerProperty(required = True)


class Profile(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/profile.html')
        self.response.out.write(template.render())



class MainHandler(webapp2.RequestHandler):
    def get(self):
    #     template = jinja_environment.get_template('templates/home.html')
    #     self.response.out.write(template.render())
        items_query = ShoppingItem.query()
        items = items_query.fetch()
        self.response.write('<ul>')
        for item in items:
            self.response.write('<li>%s (%d) </li>' % (item.name, item.quantity))
        self.response.write('</ul>')
        self.response.write('<a href = "/add_item"> Add Items</a>')
app = webapp2.WSGIApplication([
    ('/profile', Profile),
    ('/', Home),
    ('/add_item', AddItemHandler),

    ('/store_item',storeItemHandler),
    ('/home', Home)

], debug=True)
