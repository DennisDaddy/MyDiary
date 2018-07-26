import unittest
import os
from app.app import *

class MyDiaryTestCase(unittest.TestCase):  

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to mydiary', response.data)

    def tes_modify_entry(self):
        tester = app.test_client(self)
        response = tester.post('/api/v1/entries/1', content_type='application/json')
        self.assertEqual(response.status_code, 405)

if __name__ == '__main__':
    unittest.main()