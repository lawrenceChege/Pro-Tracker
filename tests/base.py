""" This is the base class for all the tests"""
from app import app
from unittest import TestCase
import unittest
import os
import json

class BaseTestCase(TestCase):
    """ set up configurations for the test environment"""
    @classmethod
    def setUpClass(cls):
        pass 

    @classmethod
    def tearDownClass(cls):
        pass 
    def setUp(self):
        """set up app configuration"""
        self.app = app.test_client(self)
        self.app.testing = True

        self.person = {
            "firstname":"lawrence",
            "lastname":"chege",
            "email":"mbuchez8@gmail.com",
            "password":"noyoudont"
        }
        self.admin ={
            "email":"admin@gmail.com",
            "password":"admin1234"
        }

        self.request={
            "category":"maintenance",
            "title":"fogort password",
            "frequency":"once",
            "description":"i am stupid"
        }

    def register_user(self):
        """Registration helper"""
        ret = self.app.post('/api/v1/auth/signup',
        data = json.dumps(self.person),
        headers = {'content-type':"appliction/json"})
        return ret
        
    def login_user(self):
        """sign in helper"""
        ret = self.app.post('/api/v1/auth/signin',
        data = json.dumps(self.person),
        headers = {'content-type':"appliction/json"})
        return ret
    
    def login_admin(self):
        """sign in helper for admin"""
        ret = self.app.post('/api/v1/auth/signin',
        data = json.dumps(self.admin),
        headers = {'content-type':"appliction/json"})
        return ret

    def logout(self):
        """Logout helper function."""
        return self.app.get('/api/v1/auth/logout', follow_redirects=True)


    def new_request(self):
        """ New  request helper"""
        ret = self.app.post('/api/v1/users-dashboard/0/0/',
        data = json.dumps(self.new_request),
        headers = {'content-type':"appliction/json"})
        return ret
    

    # def tearDown(self):
    #     USERS.clear()
    #     REQUESTS.clear()
    #     Requests.count = 0
if __name__ == '__main__':
    unittest.main()

