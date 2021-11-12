#!/usr/bin/python3
"""A unit test module for the city model.
"""
import unittest
from datetime import datetime

from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Represents the test class for the City class.
    """

    def test_init(self):
        """Tests the initialization of the City class.
        """
        self.assertIsInstance(City(), BaseModel)
        self.assertTrue(hasattr(City, 'name'))
        self.assertTrue(hasattr(City, 'state_id'))
        self.assertIsInstance(City.name, str)
        self.assertIsInstance(City.state_id, str)
        self.assertEqual(City().name, '')
        self.assertEqual(City().state_id, '')
        self.assertEqual(City('Bahia').name, '')
        self.assertEqual(City('9e45').state_id, '')
        self.assertEqual(City(name='São Paulo').name, 'São Paulo')
        self.assertEqual(City(state_id='9e45').state_id, '9e45')
        self.assertEqual(City('Bahia', name='Nevada').name, 'Nevada')
        self.assertEqual(City('12f5', state_id='9e45').state_id, '9e45')
