#!/usr/bin/python3
"""A unit test module for the review model.
"""
import unittest
from datetime import datetime

from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Represents the test class for the Review class.
    """

    def test_init(self):
        """Tests the initialization of the Review class.
        """
        self.assertIsInstance(Review(), BaseModel)
        self.assertTrue(hasattr(Review, 'place_id'))
        self.assertTrue(hasattr(Review, 'user_id'))
        self.assertTrue(hasattr(Review, 'text'))
        self.assertIsInstance(Review.place_id, str)
        self.assertIsInstance(Review.user_id, str)
        self.assertIsInstance(Review.text, str)
        self.assertEqual(Review().place_id, '')
        self.assertEqual(Review().user_id, '')
        self.assertEqual(Review().text, '')
        self.assertEqual(Review('p-e3').place_id, '')
        self.assertEqual(Review('u-a5').user_id, '')
        self.assertEqual(Review('T\'was fun').text, '')
        self.assertEqual(Review(place_id='p-e3').place_id, 'p-e3')
        self.assertEqual(Review(user_id='u-a5').user_id, 'u-a5')
        self.assertEqual(Review(text='T\'was fun').text, 'T\'was fun')
        self.assertEqual(Review('p-e8', place_id='p-e9').place_id, 'p-e9')
        self.assertEqual(Review('u-a3', user_id='u-a2').user_id, 'u-a2')
        self.assertEqual(Review('Loved it', text='GOOD').text, 'GOOD')
