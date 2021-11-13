#!/usr/bin/python3
"""A unit test module for the city model.
"""
import os
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

    def test_str(self):
        """Tests the __str__ function of the City class.
        """
        datetime_now = datetime.today()
        datetime_now_repr = repr(datetime_now)
        mdl = City()
        mdl.id = '012345'
        mdl.created_at = mdl.updated_at = datetime_now
        mdl_str = str(mdl)
        self.assertIn("[City] (012345)", mdl_str)
        self.assertIn("'id': '012345'", mdl_str)
        self.assertIn("'created_at': " + datetime_now_repr, mdl_str)
        self.assertIn("'updated_at': " + datetime_now_repr, mdl_str)
        self.assertIn("'id': ", str(City()))
        self.assertIn("'created_at': ", str(City()))
        self.assertIn("'updated_at': ", str(City()))
        self.assertIn(
            "'gender': 'female'",
            str(City(gender='female', id='m-77'))
        )
        self.assertNotIn(
            "'created_at': ",
            str(City(gender='female', id='u-88'))
        )
        self.assertNotIn(
            "'updated_at': ",
            str(City(gender='female', id='u-55'))
        )
        self.assertRegex(
            str(City()),
            r'\[City\] \([0-9a-zA-Z]+(?:-[0-9a-zA-Z]+)*\) \{.+\}'
        )
        self.assertEqual(
            str(City(id='m-345')),
            "[City] (m-345) {'id': 'm-345'}"
        )
        self.assertEqual(
            str(City(id=45)),
            "[City] (45) {'id': 45}"
        )
        self.assertEqual(
            str(City(id=None)),
            "[City] (None) {'id': None}"
        )
        with self.assertRaises(AttributeError):
            str(City(gender='female'))

    def test_to_dict(self):
        """Tests the to_dict function of the City class.
        """
        # Tests if it's a dictionary
        self.assertIsInstance(City().to_dict(), dict)
        # Tests if to_dict contains accurate keys
        self.assertIn('id', City().to_dict())
        self.assertIn('created_at', City().to_dict())
        self.assertIn('updated_at', City().to_dict())
        # Tests if to_dict contains added attributes
        mdl = City()
        mdl.firstname = 'Celestine'
        mdl.lastname = 'Akpanoko'
        self.assertIn('firstname', mdl.to_dict())
        self.assertIn('lastname', mdl.to_dict())
        self.assertIn('firstname', City(firstname='Celestine').to_dict())
        self.assertIn('lastname', City(lastname='Akpanoko').to_dict())
        # Tests to_dict datetime attributes if they are strings
        self.assertIsInstance(City().to_dict()['created_at'], str)
        self.assertIsInstance(City().to_dict()['updated_at'], str)
        # Tests to_dict output
        datetime_now = datetime.today()
        mdl = City()
        mdl.id = '012345'
        mdl.created_at = mdl.updated_at = datetime_now
        to_dict = {
            'id': '012345',
            '__class__': 'City',
            'created_at': datetime_now.isoformat(),
            'updated_at': datetime_now.isoformat()
        }
        self.assertDictEqual(mdl.to_dict(), to_dict)
        self.assertDictEqual(
            City(id='u-b34', age=13).to_dict(),
            {
                '__class__': 'City',
                'id': 'u-b34',
                'age': 13
            }
        )
        self.assertDictEqual(
            City(id='u-b34', age=None).to_dict(),
            {
                '__class__': 'City',
                'id': 'u-b34',
                'age': None
            }
        )
        # Tests to_dict output contradiction
        mdl_d = City()
        self.assertIn('__class__', City().to_dict())
        self.assertNotIn('__class__', City().__dict__)
        self.assertNotEqual(mdl_d.to_dict(), mdl_d.__dict__)
        self.assertNotEqual(
            mdl_d.to_dict()['__class__'],
            mdl_d.__class__
        )
        # Tests to_dict with arg
        with self.assertRaises(TypeError):
            City().to_dict(None)
        with self.assertRaises(TypeError):
            City().to_dict(City())
        with self.assertRaises(TypeError):
            City().to_dict(45)

    def tearDown(self):
        """Deconstructs this test class.
        """
        super().tearDown()
        if os.path.isfile('file.json'):
            os.unlink('file.json')
