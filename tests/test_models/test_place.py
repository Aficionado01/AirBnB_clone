#!/usr/bin/python3
"""A unit test module for the place model.
"""
import unittest
from datetime import datetime

from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Represents the test class for the Place class.
    """

    def test_init(self):
        """Tests the initialization of the Place class.
        """
        self.assertIsInstance(Place(), BaseModel)
        self.assertTrue(hasattr(Place, 'city_id'))
        self.assertTrue(hasattr(Place, 'user_id'))
        self.assertTrue(hasattr(Place, 'name'))
        self.assertTrue(hasattr(Place, 'description'))
        self.assertTrue(hasattr(Place, 'number_rooms'))
        self.assertTrue(hasattr(Place, 'number_bathrooms'))
        self.assertTrue(hasattr(Place, 'max_guest'))
        self.assertTrue(hasattr(Place, 'price_by_night'))
        self.assertTrue(hasattr(Place, 'latitude'))
        self.assertTrue(hasattr(Place, 'longitude'))
        self.assertTrue(hasattr(Place, 'amenity_ids'))
        self.assertIsInstance(Place.city_id, str)
        self.assertIsInstance(Place.user_id, str)
        self.assertIsInstance(Place.name, str)
        self.assertIsInstance(Place.description, str)
        self.assertIsInstance(Place.number_rooms, int)
        self.assertIsInstance(Place.number_bathrooms, int)
        self.assertIsInstance(Place.max_guest, int)
        self.assertIsInstance(Place.price_by_night, int)
        self.assertIsInstance(Place.latitude, float)
        self.assertIsInstance(Place.longitude, float)
        self.assertIsInstance(Place.amenity_ids, list)
        self.assertEqual(Place().city_id, '')
        self.assertEqual(Place().user_id, '')
        self.assertEqual(Place().name, '')
        self.assertEqual(Place().description, '')
        self.assertEqual(Place().number_rooms, 0)
        self.assertEqual(Place().number_bathrooms, 0)
        self.assertEqual(Place().max_guest, 0)
        self.assertEqual(Place().price_by_night, 0)
        self.assertEqual(Place().latitude, 0.0)
        self.assertEqual(Place().longitude, 0.0)
        self.assertEqual(Place().amenity_ids, [])
        self.assertEqual(Place('p-d62').city_id, '')
        self.assertEqual(Place('u-a98').user_id, '')
        self.assertEqual(Place('Zuba').name, '')
        self.assertEqual(Place('Majestic').description, '')
        self.assertEqual(Place(3).number_rooms, 0)
        self.assertEqual(Place(4).number_bathrooms, 0)
        self.assertEqual(Place(8).max_guest, 0)
        self.assertEqual(Place(120).price_by_night, 0)
        self.assertEqual(Place(12.3).latitude, 0.0)
        self.assertEqual(Place(56.8).longitude, 0.0)
        self.assertEqual(Place(['a-f3', 'a-c5']).amenity_ids, [])
        self.assertEqual(Place(city_id='p-d62').city_id, 'p-d62')
        self.assertEqual(Place(user_id='u-a98').user_id, 'u-a98')
        self.assertEqual(Place(name='Zuba').name, 'Zuba')
        self.assertEqual(Place(description='Scary').description, 'Scary')
        self.assertEqual(Place(number_rooms=3).number_rooms, 3)
        self.assertEqual(Place(number_bathrooms=4).number_bathrooms, 4)
        self.assertEqual(Place(max_guest=8).max_guest, 8)
        self.assertEqual(Place(price_by_night=120).price_by_night, 120)
        self.assertEqual(Place(latitude=12.3).latitude, 12.3)
        self.assertEqual(Place(longitude=56.8).longitude, 56.8)
        self.assertEqual(Place(amenity_ids=['a-f3']).amenity_ids, ['a-f3'])
        self.assertEqual(Place('p-87', city_id='p-d62').city_id, 'p-d62')
        self.assertEqual(Place('u-13', user_id='u-a98').user_id, 'u-a98')
        self.assertEqual(Place('Accra', name='Zuba').name, 'Zuba')
        self.assertEqual(Place('eh', description='Scary').description, 'Scary')
        self.assertEqual(Place(12, number_rooms=3).number_rooms, 3)
        self.assertEqual(Place(56, number_bathrooms=4).number_bathrooms, 4)
        self.assertEqual(Place(56, max_guest=8).max_guest, 8)
        self.assertEqual(Place(450, price_by_night=120).price_by_night, 120)
        self.assertEqual(Place(47.3, latitude=12.3).latitude, 12.3)
        self.assertEqual(Place(98.2, longitude=56.8).longitude, 56.8)
        self.assertEqual(Place([], amenity_ids=['a-f3']).amenity_ids, ['a-f3'])
