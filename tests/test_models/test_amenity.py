#!/usr/bin/python3
"""A unit test module for the amenity model.
"""
from datetime import datetime
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Represents the test class for the Amenity class.
    """

    def test_init(self):
        """Tests the initialization of the Amenity class.
        """
        self.assertIsInstance(Amenity(), BaseModel)
        self.assertIsInstance(Amenity().id, str)
        self.assertIsInstance(Amenity().created_at, datetime)
        self.assertIsInstance(Amenity().updated_at, datetime)
        self.assertIsInstance(Amenity().name, str)
        self.assertEqual(Amenity(name='wifi').name, 'wifi')
        self.assertEqual(Amenity('bar', name='jacuzzi').name, 'jacuzzi')
