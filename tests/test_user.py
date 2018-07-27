"""Import python modules"""
import unittest
import json
import os
import sys
from app import *

sys.path.insert(0, os.path.abspath(".."))


class MyDiaryTestCase(unittest.TestCase):
    """This test case represents test for user and diary entry testcase"""
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client

    def test_register(self):
        """"Test user registration"""
        with app.test_client(self) as toaster:
            response = toaster.post('/api/v1/auth/register',
                                    json={'username': 'dennis', 'email': 'de@gmail.com',
                                          'password': 'secret', 'password_confirmation': 'secret'})
            self.assertEqual(response.status_code, 200)

    def test_wrong_registration(self):
        """"Test user registration"""
        with app.test_client(self) as toaster:
            response = toaster.post('/api/v1/auth/register',
                                    json={'username': 'dennis', 'email': 'de@gmail.com',
                                          'password': 'secret', 'password_confirmation': 'secret'})
            self.assertEqual(response.status_code, 200)



    def test_login(self):
        """"Test logging in"""
        tester1 = app.test_client(self)
        response = tester1.post('/api/v1/auth/login',
                                json={'username' : 'dennis', 'password': 'secret'})

        self.assertEqual(response.status_code, 200)

   
    def test_user_info(self):
        """"Test user account information"""        
        response = self.client().get('/api/v1/users/1')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
