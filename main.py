import webapp2
from google.appengine.ext import ndb
import logging
import jinja2
import os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))



add_item_from = '''
<form action = "store_user" method = "post">
    first_name: <input type = "text" name = "first_name"/><br>
    last_name: <input type = "text" name = "last_name" /> <br>
    age: <input type = "text" name = "age" /> <br>
    favorite_sport: <input type = "text" name = "favorite_sport"/> <br>
         <input type = "submit"/>
</form>

'''

class UserInfo(ndb.Model):
    email = ndb.StringProperty(required = True)
    first_name = ndb.StringProperty(required = True)
    last_name = ndb.StringProperty(required = True)
    age = ndb.IntegerProperty(required = True)
    favorite_sport = ndb.StringProperty(required = True)


class StoreUserHandler(webapp2.RequestHandler):
    def post(self):
        user_email = self.request.get('email')
        user_f_name = self.request.get('first_name')
        user_l_name = self.request.get('last_name')
        user_age = int(self.request.get('age'))
        fav_sport = self.request.get('favorite_sport')

        existing_item_query = UserInfo.query((UserInfo.first_name == user_f_name) and (UserInfo.last_name == user_l_name))
        existing_item = existing_item_query.get()
        if existing_item is not None:
              existing_item.put()
        else:
            item = UserInfo(email = user_email, first_name = user_f_name, last_name = user_l_name, age = user_age,favorite_sport = fav_sport)
            key = item.put()
            logging.info('The key for the item %s is %s' % (item,key))
        self.redirect('/')

class AddUserHandler(webapp2.RequestHandler):
    def get(self):
         self.response.write(add_item_from)

class SignIn(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("templates/profile.html")
        '''
        users_query = UserInfo.query()
        users = users_query.fetch()
        self.response.write('<ul>')
        for user in users:

            self.response.write('<li>{} {} {} {} </li>'.format(user.email,user.first_name, user.last_name, user.age, user.favorite_sport))

        self.response.write('</ul>')
        self.response.write('<a href = "/add_user"> Add User</a>')
        '''
        self.response.write(template.render())

    def post(self):
        template = jinja_environment.get_template("templates/home.html")
        user_email = self.request.get('email')
        user_f_name = self.request.get('first_name')
        user_l_name = self.request.get('last_name')
        user_age = int(self.request.get('age'))
        fav_sport = self.request.get('favorite_sport')
        info = {"email": user_email,"first_name": user_f_name,"last_name":user_l_name, "age":user_age, "favorite_sport":fav_sport}

        self.response.write(template.render(info))

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/profile.html')
        self.response.out.write(template.render())


app = webapp2.WSGIApplication([
    ('/', SignIn),
    ('/main', MainPage),
    ('/add_user', AddUserHandler),
    ('/store_user',StoreUserHandler)

], debug=True)
