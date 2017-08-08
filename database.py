from google.appengine.ext import ndb

class User(ndb.Model):
    name = ndb.StringProperty()
    age = ndb.StringProperty()
    birthday = ndb.DateProperty()
    favorite_sport = nbd.StringProperty()
