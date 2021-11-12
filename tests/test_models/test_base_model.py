#!/usr/bin/python3
"""A unit test module for the base model of all models.
"""
import unittest
from datetime import datetime
import re
import os
import time
from time import sleep

from models.base_model import BaseModel
from tests import remove_files


class TestBaseModel(unittest.TestCase):
    """Represents the test class for the BaseModel class.
    """

    def test_init(self):
        """Tests the initialization of the Base class.
        """
        self.assertTrue(hasattr(BaseModel(), 'id'))
        self.assertTrue(hasattr(BaseModel(), 'created_at'))
        self.assertTrue(hasattr(BaseModel(), 'updated_at'))
        self.assertIsInstance(BaseModel().id, str)
        self.assertIsInstance(BaseModel().created_at, datetime)
        self.assertIsInstance(BaseModel().updated_at, datetime)
        # No args instantiated
        self.assertEqual(BaseModel, type(BaseModel()))
        # Tests for the uniqueness in ID's
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)
        # Tests for differences in created time
        bm3 = BaseModel()
        sleep(0.06)
        bm4 = BaseModel()
        self.assertLess(bm3.created_at, bm4.created_at)
        # Tests for differences in updated time
        bm3 = BaseModel()
        sleep(0.06)
        bm4 = BaseModel()
        self.assertLess(bm3.updated_at, bm4.updated_at)
        # Tests for unused args
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

        # Tests instantiation with kwargs
        datetime_now = datetime.today()
        datetime_now_iso = datetime_now.isoformat()
        bm = BaseModel(id='012', created_at=datetime_now_iso,
                       updated_at=datetime_now_iso)
        self.assertEqual(bm.id, '012')
        self.assertEqual(bm.created_at, datetime_now)
        self.assertEqual(bm.updated_at, datetime_now)

        # Tests instantiations with None kwargs
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

        # Tests instantiation with args and kwargs
        datetime_now = datetime.today()
        datetime_now_iso = datetime_now.isoformat()
        bm = BaseModel('01', id='012', created_at=datetime_now_iso,
                       updated_at=datetime_now_iso)
        self.assertEqual(bm.id, '012')
        self.assertEqual(bm.created_at, datetime_now)
        self.assertEqual(bm.updated_at, datetime_now)

    def test_str(self):
        """Tests the string representation of BaseModel instance
        """
        datetime_now = datetime.today()
        datetime_now_repr = repr(datetime_now)
        bm = BaseModel()
        bm.id = '012345'
        bm.created_at = bm.updated_at = datetime_now
        bm_str = bm.__str__()
        self.assertIn("[BaseModel] (012345)", bm_str)
        self.assertIn("'id': '012345'", bm_str)
        self.assertIn("'created_at': " + datetime_now_repr, bm_str)
        self.assertIn("'updated_at': " + datetime_now_repr, bm_str)

    def test_save(self):
        """Tests the save function of the BaseModel class.
        """
        # Tries to rename a file and delete it
        try:
            os.rename('file.json', 'random_name')
        except IOError:
            pass
        try:
            os.remove('file.json')
        except IOError:
            pass
        try:
            os.rename('random_name', 'file.json')
        except IOError:
            pass

        # Tests for a single save
        bm = BaseModel()
        sleep(0.06)
        updated_at_1 = bm.updated_at
        bm.save()
        self.assertLess(updated_at_1, bm.updated_at)

        # Tests for a double save
        bm = BaseModel()
        sleep(0.06)
        updated_at_1 = bm.updated_at
        bm.save()
        updated_at_2 = bm.updated_at
        self.assertLess(updated_at_1, updated_at_2)
        sleep(0.06)
        bm.save()
        self.assertLess(updated_at_2, bm.updated_at)

        # Tests save with args
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

        # Tests save updates on file
        bm = BaseModel()
        bm.save()
        bm_id = 'BaseModel.' + bm.id
        with open('file.json', 'r') as f:
            self.assertIn(bm_id, f.read())

    def test_to_dict(self):
        """Tests the to_dict function of the BaseModel class.
        """
        # Tests if it's a dictionary
        bm = BaseModel()
        self.assertTrue(dict, type(bm.to_dict()))

        # Tests if to_dict contains accurate keys
        self.assertIn('id', bm.to_dict())
        self.assertIn('created_at', bm.to_dict())
        self.assertIn('updated_at', bm.to_dict())
        self.assertIn('__class__', bm.to_dict())

        # Tests if to_dict contains added attributes
        bm.firstname = 'Celestine'
        bm.lastname = 'Akpanoko'
        self.assertIn('firstname', bm.to_dict())
        self.assertIn('lastname', bm.to_dict())

        # Tests to_dict datetime attributes if they are strings
        bm_dict = bm.to_dict()
        self.assertEqual(str, type(bm_dict['created_at']))
        self.assertEqual(str, type(bm_dict['updated_at']))

        # Tests to_dict output
        datetime_now = datetime.today()
        bm = BaseModel()
        bm.id = '012345'
        bm.created_at = bm.updated_at = datetime_now
        to_dict = {
            'id': '012345',
            '__class__': 'BaseModel',
            'created_at': datetime_now.isoformat(),
            'updated_at': datetime_now.isoformat()
        }
        self.assertDictEqual(bm.to_dict(), to_dict)
        # Tests to_dict output contradiction
        bm_d = BaseModel()
        self.assertNotEqual(bm_d.to_dict(), bm_d.__dict__)

        # Tests to_dict with arg
        with self.assertRaises(TypeError):
            bm_d.to_dict(None)


if __name__ == __main__:
    unittest.main()
