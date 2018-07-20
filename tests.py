"""Import python modules"""
import unittest

from app import app



class MyDiaryTestCase(unittest.TestCase):
    """This test case represents test for user and diary entry testcase"""
    def test_index(self):
        """"Test root endpoint"""
        tester = app.test_client(self)
        response = tester.get('/', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to mydiary', response.data)

    def test_register(self):
        """"Test user registration"""
        with app.test_client(self) as toaster:
            response = toaster.post('/diary/api/v1/auth/register',
                                    json={'username': 'dennis', 'email': 'de@gmail.com',
                                          'password': 'secret', 'password_confirmation': 'secret'})
            self.assertEqual(response.status_code, 200)
    def test_create_entry(self):
        """Test entry creation"""
        tester = app.test_client(self)
        self.assertEqual(tester.post('/diary/api/v1/entries',
                                     data=dict(title="New", content="entry"),
                                     follow_redirects=True).status_code, 200)

    def test_delete_entry(self):
        """"Test entry deletion"""
        tester = app.test_client(self)
        self.assertEqual(tester.delete('/diary/api/v1/entries/1',
                                       content_type='application/json').status_code, 200)

    def test_view_entries(self):
        """"Test listing all entries"""
        with app.test_client(self) as tester:
            response = tester.get('/diary/api/v1/entries', content_type='application/json')
            self.assertEqual(response.status_code, 200)

    def test_modify_entry(self):
        """"Test entry modification"""
        tester2 = app.test_client(self)
        response = tester2.get('/diary/api/v1/entries/1', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_view_entry(self):
        """"Test entry details"""
        tester = app.test_client(self)
        response = tester.get('/diary/api/v1/entries/1', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        """"Test logging in"""
        tester1 = app.test_client(self)
        response = tester1.post('/diary/api/v1/auth/login',
                                json={'username' : 'dennis', 'password': 'secret'})

        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        """"Test logging out"""
        with app.test_client(self) as tester:
            response = tester.delete('/logout', content_type='application/json')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'you are successfully logged out', response.data)
    def test_user_info(self):
        """"Test user account information"""
        tester = app.test_client(self)
        response = tester.get('/diary/api/v1/account')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
