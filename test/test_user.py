import unittest
import os
from app.app import *

class MyDiaryTestCase(unittest.TestCase):

     def setUp(self):
        """Initialize test variables"""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.entry = {
            'username': "dennis",
            'email': "dennis@gmail.com",
            'password': "123456",
            'password_confirmation': "123456"

        }


    def tes_user_register_entry(self):
        tester = app.test_client(self)
        response = tester.post('/api/v1/auth/register', content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def tes_user_login_entry(self):
        tester = app.test_client(self)
        response = tester.put('/api/v1/auth/register', content_type='application/json')
        self.assertEqual(response.status_code, 201)    



if __name__ == '__main__':
    unittest.main()