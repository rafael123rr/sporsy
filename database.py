from google.appengine.ext import ndb

class User(ndb.Model):
    name = ndb.StringProperty()
    age = ndb.IntProperty()
    birthday = ndb.DateProperty()
    favorite_sport = nbd.StringProperty()
