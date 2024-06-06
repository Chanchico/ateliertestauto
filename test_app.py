import unittest
import requests

class BookTestCase(unittest.TestCase):

    def test_create_book(self):
        response = requests.post('http://127.0.0.1:5000/book', json={
            'title': 'The Great Gatsby',
            'author': 'F. Scott Fitzgerald',
            'isbn': '9780743273565',
            'description': 'A novel set in the Jazz Age'
        }, headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertEqual(data['title'], 'The Great Gatsby')
        self.assertEqual(data['author'], 'F. Scott Fitzgerald')
        self.assertEqual(data['isbn'], '9780743273565')
        self.assertEqual(data['description'], 'A novel set in the Jazz Age')

    def test_get_books(self):
        response = requests.get('http://127.0.0.1:5000/books')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['title'], 'The Great Gatsby')

    def test_get_book(self):
        response = requests.get('http://127.0.0.1:5000/book/1')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['title'], 'The Great Gatsby')

    def test_update_book(self):
        response = requests.put('http://127.0.0.1:5000/book/1', json={
            'title': 'The Great Gatsby - Updated',
            'author': 'F. Scott Fitzgerald',
            'isbn': '9780743273565',
            'description': 'A novel set in the Jazz Age - Updated'
        }, headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['title'], 'The Great Gatsby - Updated')

    def test_delete_book(self):
        response = requests.delete('http://127.0.0.1:5000/book/1', headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
