#!/usr/bin/python3
"""A unit test module for the amenity model.
"""
import os
import unittest
from datetime import datetime

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

    def test_str(self):
        """Tests the __str__ function of the Amenity class.
        """
        datetime_now = datetime.today()
        datetime_now_repr = repr(datetime_now)
        mdl = Amenity()
        mdl.id = '012345'
        mdl.created_at = mdl.updated_at = datetime_now
        mdl_str = str(mdl)
        self.assertIn("[Amenity] (012345)", mdl_str)
        self.assertIn("'id': '012345'", mdl_str)
        self.assertIn("'created_at': " + datetime_now_repr, mdl_str)
        self.assertIn("'updated_at': " + datetime_now_repr, mdl_str)
        self.assertIn("'id': ", str(Amenity()))
        self.assertIn("'created_at': ", str(Amenity()))
        self.assertIn("'updated_at': ", str(Amenity()))
        self.assertIn(
            "'gender': 'female'",
            str(Amenity(gender='female', id='m-77'))
        )
        self.assertNotIn(
            "'created_at': ",
            str(Amenity(gender='female', id='u-88'))
        )
        self.assertNotIn(
            "'updated_at': ",
            str(Amenity(gender='female', id='u-55'))
        )
        self.assertRegex(
            str(Amenity()),
            r'\[Amenity\] \([0-9a-zA-Z]+(?:-[0-9a-zA-Z]+)*\) \{.+\}'
        )
        self.assertEqual(
            str(Amenity(id='m-345')),
            "[Amenity] (m-345) {'id': 'm-345'}"
        )
        self.assertEqual(
            str(Amenity(id=45)),
            "[Amenity] (45) {'id': 45}"
        )
        self.assertEqual(
            str(Amenity(id=None)),
            "[Amenity] (None) {'id': None}"
        )
        with self.assertRaises(AttributeError):
            str(Amenity(gender='female'))

    def test_to_dict(self):
        """Tests the to_dict function of the Amenity class.
        """
        # Tests if it's a dictionary
        self.assertIsInstance(Amenity().to_dict(), dict)
        # Tests if to_dict contains accurate keys
        self.assertIn('id', Amenity().to_dict())
        self.assertIn('created_at', Amenity().to_dict())
        self.assertIn('updated_at', Amenity().to_dict())
        # Tests if to_dict contains added attributes
        mdl = Amenity()
        mdl.firstname = 'Celestine'
        mdl.lastname = 'Akpanoko'
        self.assertIn('firstname', mdl.to_dict())
        self.assertIn('lastname', mdl.to_dict())
        self.assertIn('firstname', Amenity(firstname='Celestine').to_dict())
        self.assertIn('lastname', Amenity(lastname='Akpanoko').to_dict())
        # Tests to_dict datetime attributes if they are strings
        self.assertIsInstance(Amenity().to_dict()['created_at'], str)
        self.assertIsInstance(Amenity().to_dict()['updated_at'], str)
        # Tests to_dict output
        datetime_now = datetime.today()
        mdl = Amenity()
        mdl.id = '012345'
        mdl.created_at = mdl.updated_at = datetime_now
        to_dict = {
            'id': '012345',
            '__class__': 'Amenity',
            'created_at': datetime_now.isoformat(),
            'updated_at': datetime_now.isoformat()
        }
        self.assertDictEqual(mdl.to_dict(), to_dict)
        self.assertDictEqual(
            Amenity(id='u-b34', age=13).to_dict(),
            {
                '__class__': 'Amenity',
                'id': 'u-b34',
                'age': 13
            }
        )
        self.assertDictEqual(
            Amenity(id='u-b34', age=None).to_dict(),
            {
                '__class__': 'Amenity',
                'id': 'u-b34',
                'age': None
            }
        )
        # Tests to_dict output contradiction
        mdl_d = Amenity()
        self.assertIn('__class__', Amenity().to_dict())
        self.assertNotIn('__class__', Amenity().__dict__)
        self.assertNotEqual(mdl_d.to_dict(), mdl_d.__dict__)
        self.assertNotEqual(
            mdl_d.to_dict()['__class__'],
            mdl_d.__class__
        )
        # Tests to_dict with arg
        with self.assertRaises(TypeError):
            Amenity().to_dict(None)
        with self.assertRaises(TypeError):
            Amenity().to_dict(Amenity())
        with self.assertRaises(TypeError):
            Amenity().to_dict(45)

    def tearDown(self):
        """Deconstructs this test class.
        """
        super().tearDown()
        if os.path.isfile('file.json'):
            os.unlink('file.json')
