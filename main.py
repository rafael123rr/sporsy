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
from database import User





class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout_link = users.create_logout_url('/')
            logging.info('The user is logged in')
            user_id = user.user_id()
            if user_id not in users_data:
                self.response.write(register_form)
                return
            name = User('name')
            age = User('age')
            birthday = User('birthday')
            favorite_sport = User('favorite_sport')

            self.response.write('Hello %s !' %
            (name)
            )





    def post(self):
        player = User(name = self.request.get("name"), age=self.request.get("age"), birthday = self.request. )
        key = student.put()
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
