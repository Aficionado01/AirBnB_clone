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
        self.assertTrue(hasattr(Amenity, 'name'))
        self.assertIsInstance(Amenity.name, str)
        self.assertEqual(Amenity().name, '')
        self.assertEqual(Amenity('swimming pool').name, '')
        self.assertEqual(Amenity(name='wifi').name, 'wifi')
        self.assertEqual(Amenity('bar', name='jacuzzi').name, 'jacuzzi')
