import unittest
from app import *

import json

class EntryTestCase(unittest.TestCase):
    def test_entry(self):
        tester = app.test_client(self)
        response = tester.get('/diary/api/v1/entries/1', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        json_data = json.loads(response.data)
    






if __name__ == '__main__':
    unittest.main()