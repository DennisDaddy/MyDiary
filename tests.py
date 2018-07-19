import unittest
from app import *

import json

class EntryTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to mydiary', response.data)

    def test_register(self):
        with app.test_client(self) as ts:
            response = ts.post('/diary/api/v1/auth/register', json={'username': 'dennis','email': 'de@gmail.com',
            'password': 'secret', 'password_confirmation': 'secret'})
            json_data = response.get_json()
            self.assertEqual(response.status_code, 200)

   
    def test_create_entry(self):
		tester = app.test_client(self)
		
		self.assertEqual(tester.post('/diary/api/v1/entries',
			data=dict(title="New", content="entry"),
			follow_redirects =True
		).status_code, 200)

    def test_delete_entry(self):
        tester = app.test_client(self)
        
        self.assertEqual(tester.delete('/diary/api/v1/entries/1', content_type='application/json').status_code, 200)


    def test_view_entries(self):
        with app.test_client(self) as tester:
            response = tester.get('/diary/api/v1/entries', content_type='application/json')
            self.assertEqual(response.status_code, 200)

    def test_modify_entry(self):
        rm = app.test_client(self)
        response = rm.get('/diary/api/v1/entries/1', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_view_entry(self):
        ls = app.test_client(self)
        response = ls.get('/diary/api/v1/entries/1', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        json_data = json.loads(response.data)
    

   
    
    def test_login(self):
        vm = app.test_client(self)
        response = vm.post('/diary/api/v1/auth/login', json={'username' : 'dennis', 'password': 'secret'})
        json_data = response.get_json()
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        with app.test_client(self) as tester:
            response = tester.delete('/logout', content_type='application/json')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'you are successfully logged out', response.data)

    
    
    
    def test_user_info(self):
        tester = app.test_client(self)
        response = tester.get('/diary/api/v1/account')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()