import unittest
import os
from app.app import *

class MyDiaryTestCase(unittest.TestCase):  

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to mydiary', response.data)

    def tes_create_entry(self):
        tester = app.test_client(self)
        response = tester.post('/api/v1/entries/', content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def tes_modify_entry(self):
        tester = app.test_client(self)
        response = tester.put('/api/v1/entries/1', content_type='application/json')
        self.assertEqual(response.status_code, 201)    

    def tes_view_entry(self):
        tester = app.test_client(self)
        response = tester.get('/api/v1/entries/1', content_type='application/json')
        self.assertEqual(response.status_code, 200)
    
    def tes_view_all_entries(self):
        tester = app.test_client(self)
        response = tester.get('/api/v1/entries', content_type='application/json')
        self.assertEqual(response.status_code, 200)
    
    def tes_delete_entries(self):
        tester = app.test_client(self)
        response = tester.delete('/api/v1/entries/1', content_type='application/json')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()