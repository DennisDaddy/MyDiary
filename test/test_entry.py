import unittest
import os

from app import create_app
class MyDiaryTestCase(unittest.TestCase):  

    def setUp(self):
        """Initialize test variables"""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.entry = {
            'title': "this one is also a title",
            'content': "This is another title"
           
        }

    def test_index(self):
        
        response = self.client.get('/', content_type='application/json')
        self.assertEqual(response.status_code, 200, {})
        self.assertIn(b'Welcome to mydiary', response.data)

    def tearDown(self):
        """Teardown enrty"""
        del self.entry
        

   
if __name__ == '__main__':
    unittest.main()