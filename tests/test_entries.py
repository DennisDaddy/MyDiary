"""Import python modules"""
import unittest
import json
import os
import sys
from app import create_app

sys.path.insert(0, os.path.abspath(".."))


class EntrylistTestCase(unittest.TestCase):
    """This test case represents test for user and diary entry testcase"""


    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.entry = {
            'title': 'This is cool one',
            'content': 'This one also is amazing'}

    def test_entry_creation(self):
        """Test creating an entry"""
        tester = self.client().post('/api/v1/entries', data=self.entry)
        self.assertEqual(tester.status_code, 201)
        self.assertIn('This is cool', str(tester.data))
        self.assertIn('This one also', str(tester.data))

    def test__view_entries(self):
        """Test retrieving all entries."""
        response = self.client().post('/api/v1/entries', data=self.entry)
        self.assertEqual(response.status_code, 201)
        response = self.client().get('/api/v1/entries')
        self.assertEqual(response.status_code, 200)
        self.assertIn('This one also', str(response.data))

    def test_single_entry(self):
        """Test retrieving single entry"""
        tester = self.client().post('/api/v1/entries', data=self.entry)
        self.assertEqual(tester.status_code, 201)
        result_in_json = json.loads(tester.data.decode('utf-8').replace("'", "\""))
        result = self.client().get(
            '/api/v1/entries/{}'.format(result_in_json['id']))
        self.assertEqual(result.status_code, 200)
        self.assertIn('This one also', str(result.data))

    def test_modify_entry(self):
        """Test entry modification"""
        response = self.client().post(
            '/bucketlists/',
            data={'title': 'walk you path'})
        self.assertEqual(response.status_code, 201)
        response = self.client().put(
            '/api/v1/entries/1',
            data={
                "title": "this was great)"
            })
        self.assertEqual(response.status_code, 200)
        results = self.client().get('/api/v1/entries/1')
        self.assertIn('Dont just eat', str(results.data))

    def test_delete_entry(self):
        """Test entry deletion"""
        response = self.client().post(
            '/api/v1/entries',
            data={'title': 'they were great'})
        self.assertEqual(response.status_code, 201)
        res = self.client().delete('/api/v1/entries/1')
        self.assertEqual(res.status_code, 200)

if __name__ == '__main__':
    unittest.main()
