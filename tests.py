import unittest
from app import app
import psycopg2
import json

class MyDiaryTestCase(unittest.TestCase):

    def setUp(self):
        tester = app.test_client(self)
        self.entry = {
            'title': 'This is title',
            'content': 'Thi is content'
        }

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='aplication/json')
        self.assertEqual(b'Welcome to MyDiary', response.data)

    def test_create_entry(self):
        tester = app.test_client().post('/api/v1/entries', data=self.entry)
        self.assertEqual(tester.status_code, 201)
        self.assertIn('This is', str(tester.data))
        
    
    def test_view_entry(self):
        tester = app.test_client().post('/api/v1/entries/1', data=self.entry)
        self.assertEqual(tester.status_code, 201)
        result_in_json = json.loads(tester.data.decode('utf-8').replace("'", "\""))
        result = tester.client().get(
            '/api/v1/entries/{}'.format(result_in_json['id'])
        )
        self.assertEqual(result.status_code, 200)
        self.assertIn('This is', str(tester.data))
        
    
    def test_view_all_entries(self):
        tester = app.test_client().post('/api/v1/entries', data=self.entry)
        self.assertEqual(tester.status_code, 201)
        tester = tester.client().get('/api/v1/entrie')
        self.assertEqual(tester.status_code, 200)
        self.assertIn('This is', str(tester.data))
        
    
    def test_delete_entry(self):
        tester = app.test_client().post('/api/v1/entries/1', data=self.entry)
        self.assertEqual(tester.status_code, 201)
        result_in_json = json.loads(tester.data.decode('utf-8').replace("'", "\""))
        result = tester.client().get(
            '/api/v1/entries/{}'.format(result_in_json['id'])
        )
        self.assertEqual(result.status_code, 200)
        self.assertIn('This is', str(tester.data))




if __name__ == '__main__':
    unittest.main()