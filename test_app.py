# EXERCICE 5-2

import unittest
import json
from app import app, db, Book

class BookTestCase(unittest.TestCase):

    def test_create_book(self):
        
        with app.test_client() as client:
            response = client.post('/book', json={
                'title': 'The Great Gatsby',
                'author': 'F. Scott Fitzgerald',
                'isbn': '9780743273565',
                'description': 'A novel set in the Jazz Age'
            })
            self.assertEqual(response.status_code, 201)
            data = json.loads(response.data)
            self.assertEqual(data['title'], 'The Great Gatsby')
            self.assertEqual(data['author'], 'F. Scott Fitzgerald')
            self.assertEqual(data['isbn'], '9780743273565')
            self.assertEqual(data['description'], 'A novel set in the Jazz Age')

    def test_get_books(self):
        with app.test_client() as client:
            client.post('/book', json={
                'title': 'The Great Gatsby',
                'author': 'F. Scott Fitzgerald',
                'isbn': '9780743273565',
                'description': 'A novel set in the Jazz Age'
            })
            response = client.get('/books')
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]['title'], 'The Great Gatsby')

    def test_get_book(self):
        with app.test_client() as client:
            client.post('/book', json={
                'title': 'The Great Gatsby',
                'author': 'F. Scott Fitzgerald',
                'isbn': '9780743273565',
                'description': 'A novel set in the Jazz Age'
            })
            response = client.get('/book/1')
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data)
            self.assertEqual(data['title'], 'The Great Gatsby')

    def test_update_book(self):
        with app.test_client() as client:
            client.post('/book', json={
                'title': 'The Great Gatsby',
                'author': 'F. Scott Fitzgerald',
                'isbn': '9780743273565',
                'description': 'A novel set in the Jazz Age'
            })
            response = client.put('/book/1', json={
                'title': 'The Great Gatsby - Updated',
                'author': 'F. Scott Fitzgerald',
                'isbn': '9780743273565',
                'description': 'A novel set in the Jazz Age - Updated'
            })
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data)
            self.assertEqual(data['title'], 'The Great Gatsby - Updated')

    def test_delete_book(self):
        with app.test_client() as client:
            client.post('/book', json={
                'title': 'The Great Gatsby',
                'author': 'F. Scott Fitzgerald',
                'isbn': '9780743273565',
                'description': 'A novel set in the Jazz Age'
            })
            response = client.delete('/book/1')
            self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
