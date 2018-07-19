import unittest
from app import *

import json

class EntryTestCase(unittest.TestCase):
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        assert b'Welcome to mydiary' in response.data






if __name__ == '__main__':
    unittest.main()