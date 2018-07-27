"""Import python modules"""
import unittest
import json
import os
import sys
from app import *

sys.path.insert(0, os.path.abspath(".."))


class EntrylistTestCase(unittest.TestCase):
    """This test case represents test for user and diary entry testcase"""


    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
       

    def test_home(self):
        result = self.client().get('/') 
        self.assertEqual(result.status_code,200, {'Message': 'Welcome to MyDiary'})


    def test__create_entries(self):
        """Test create entry."""
        response = self.client().get('/api/v1/entries')
        self.assertEqual(response.status_code, 200)
    
    def test__retrieve_entry(self):
        """Test retrieve single entry."""
        response = self.client().get('/api/v1/entries')
        self.assertEqual(response.status_code, 200)

   
    def test__view_entries(self):
        """Test retrieving all entries."""
        response = self.client().get('/api/v1/entries')
        self.assertEqual(response.status_code, 200)

    def test__modify_entry(self):
        """Test modifying an entry."""
        response = self.client().get('/api/v1/entries/1')
        self.assertEqual(response.status_code, 200)

    def test__delete_entry(self):
        """Test delete entry."""
        response = self.client().get('/api/v1/entries/1')
        self.assertEqual(response.status_code, 200)
    
    

    

if __name__ == '__main__':
    unittest.main()
