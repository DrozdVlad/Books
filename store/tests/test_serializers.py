from django.test import TestCase

from store.models import Book
from store.serializers import BookSerializer


class BookSerializersTestCase(TestCase):
    def test_ok(self):
        book_1 = Book.objects.create(name='Harry Potter ', price=15)
        book_2 = Book.objects.create(name='Parrot', price=21)
        data = BookSerializer([book_1, book_2], many=True).data
        expected_data = \
            [
                {
                    'id': book_1.id,
                    'name': 'Harry Potter ',
                    'price': '15.00'
                },
                {
                    'id': book_2.id,
                    'name': 'Parrot',
                    'price': '21.00'
                }
            ]
        self.assertEqual(expected_data, data)