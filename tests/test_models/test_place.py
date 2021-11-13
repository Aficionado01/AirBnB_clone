#!/usr/bin/python3
"""A unit test module for the place model.
"""
import os
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

    def test_str(self):
        """Tests the __str__ function of the Place class.
        """
        datetime_now = datetime.today()
        datetime_now_repr = repr(datetime_now)
        mdl = Place()
        mdl.id = '012345'
        mdl.created_at = mdl.updated_at = datetime_now
        mdl_str = str(mdl)
        self.assertIn("[Place] (012345)", mdl_str)
        self.assertIn("'id': '012345'", mdl_str)
        self.assertIn("'created_at': " + datetime_now_repr, mdl_str)
        self.assertIn("'updated_at': " + datetime_now_repr, mdl_str)
        self.assertIn("'id': ", str(Place()))
        self.assertIn("'created_at': ", str(Place()))
        self.assertIn("'updated_at': ", str(Place()))
        self.assertIn(
            "'gender': 'female'",
            str(Place(gender='female', id='m-77'))
        )
        self.assertNotIn(
            "'created_at': ",
            str(Place(gender='female', id='u-88'))
        )
        self.assertNotIn(
            "'updated_at': ",
            str(Place(gender='female', id='u-55'))
        )
        self.assertRegex(
            str(Place()),
            r'\[Place\] \([0-9a-zA-Z]+(?:-[0-9a-zA-Z]+)*\) \{.+\}'
        )
        self.assertEqual(
            str(Place(id='m-345')),
            "[Place] (m-345) {'id': 'm-345'}"
        )
        self.assertEqual(
            str(Place(id=45)),
            "[Place] (45) {'id': 45}"
        )
        self.assertEqual(
            str(Place(id=None)),
            "[Place] (None) {'id': None}"
        )
        with self.assertRaises(AttributeError):
            str(Place(gender='female'))

    def test_to_dict(self):
        """Tests the to_dict function of the Place class.
        """
        # Tests if it's a dictionary
        self.assertIsInstance(Place().to_dict(), dict)
        # Tests if to_dict contains accurate keys
        self.assertIn('id', Place().to_dict())
        self.assertIn('created_at', Place().to_dict())
        self.assertIn('updated_at', Place().to_dict())
        # Tests if to_dict contains added attributes
        mdl = Place()
        mdl.firstname = 'Celestine'
        mdl.lastname = 'Akpanoko'
        self.assertIn('firstname', mdl.to_dict())
        self.assertIn('lastname', mdl.to_dict())
        self.assertIn('firstname', Place(firstname='Celestine').to_dict())
        self.assertIn('lastname', Place(lastname='Akpanoko').to_dict())
        # Tests to_dict datetime attributes if they are strings
        self.assertIsInstance(Place().to_dict()['created_at'], str)
        self.assertIsInstance(Place().to_dict()['updated_at'], str)
        # Tests to_dict output
        datetime_now = datetime.today()
        mdl = Place()
        mdl.id = '012345'
        mdl.created_at = mdl.updated_at = datetime_now
        to_dict = {
            'id': '012345',
            '__class__': 'Place',
            'created_at': datetime_now.isoformat(),
            'updated_at': datetime_now.isoformat()
        }
        self.assertDictEqual(mdl.to_dict(), to_dict)
        self.assertDictEqual(
            Place(id='u-b34', age=13).to_dict(),
            {
                '__class__': 'Place',
                'id': 'u-b34',
                'age': 13
            }
        )
        self.assertDictEqual(
            Place(id='u-b34', age=None).to_dict(),
            {
                '__class__': 'Place',
                'id': 'u-b34',
                'age': None
            }
        )
        # Tests to_dict output contradiction
        mdl_d = Place()
        self.assertIn('__class__', Place().to_dict())
        self.assertNotIn('__class__', Place().__dict__)
        self.assertNotEqual(mdl_d.to_dict(), mdl_d.__dict__)
        self.assertNotEqual(
            mdl_d.to_dict()['__class__'],
            mdl_d.__class__
        )
        # Tests to_dict with arg
        with self.assertRaises(TypeError):
            Place().to_dict(None)
        with self.assertRaises(TypeError):
            Place().to_dict(Place())
        with self.assertRaises(TypeError):
            Place().to_dict(45)

    def tearDown(self):
        """Deconstructs this test class.
        """
        super().tearDown()
        if os.path.isfile('file.json'):
            os.unlink('file.json')
