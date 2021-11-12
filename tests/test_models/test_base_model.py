#!/usr/bin/python3
"""A unit test module for the base model of all models.
"""
import os
import unittest
from datetime import datetime
from time import sleep

from models.base_model import BaseModel
from tests import remove_files


class TestBaseModel(unittest.TestCase):
    """Represents the test class for the BaseModel class.
    """

    def test_init(self):
        """Tests the initialization of the BaseModel class.
        """
        self.assertFalse(hasattr(BaseModel, 'id'))
        self.assertFalse(hasattr(BaseModel, 'created_at'))
        self.assertFalse(hasattr(BaseModel, 'updated_at'))
        self.assertTrue(hasattr(BaseModel(), 'id'))
        self.assertTrue(hasattr(BaseModel(), 'created_at'))
        self.assertTrue(hasattr(BaseModel(), 'updated_at'))
        self.assertIsInstance(BaseModel().id, str)
        self.assertIsInstance(BaseModel().created_at, datetime)
        self.assertIsInstance(BaseModel().updated_at, datetime)
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
        self.assertEqual(BaseModel(id=45).id, 45)
        self.assertEqual(BaseModel(id=None).id, None)
        self.assertNotEqual(BaseModel('cc5f').id, 'cc5f')
        self.assertNotEqual(BaseModel('cc5f').created_at, 'cc5f')
        self.assertNotEqual(BaseModel('cc5f').updated_at, 'cc5f')
        self.assertTrue(hasattr(BaseModel(foo=45), 'foo'))
        self.assertFalse(hasattr(BaseModel(foo=45), 'id'))
        self.assertFalse(hasattr(BaseModel(foo=45), 'created_at'))
        self.assertFalse(hasattr(BaseModel(foo=45), 'updated_at'))
        self.assertNotEqual(BaseModel(__class__='45').__class__, '45')
        self.assertNotEqual(BaseModel(__class__=None).__class__, None)
        with self.assertRaises(TypeError):
            BaseModel(**{'created_at': 45})
        with self.assertRaises(TypeError):
            BaseModel(**{'created_at': datetime.now()})
        with self.assertRaises(TypeError):
            BaseModel(**{'updated_at': 45})
        with self.assertRaises(TypeError):
            BaseModel(**{'updated_at': datetime.now()})

    def test_str(self):
        """Tests the __str__ function of the BaseModel class.
        """
        datetime_now = datetime.today()
        datetime_now_repr = repr(datetime_now)
        bm = BaseModel()
        bm.id = '012345'
        bm.created_at = bm.updated_at = datetime_now
        bm_str = str(bm)
        self.assertIn("[BaseModel] (012345)", bm_str)
        self.assertIn("'id': '012345'", bm_str)
        self.assertIn("'created_at': " + datetime_now_repr, bm_str)
        self.assertIn("'updated_at': " + datetime_now_repr, bm_str)
        self.assertIn(
            "'id': ",
            str(BaseModel())
        )
        self.assertIn(
            "'created_at': ",
            str(BaseModel())
        )
        self.assertIn(
            "'updated_at': ",
            str(BaseModel())
        )
        self.assertIn(
            "'gender': ",
            str(BaseModel(gender='female', id='m-77'))
        )
        self.assertNotIn(
            "'created_at': ",
            str(BaseModel(gender='female', id='u-88'))
        )
        self.assertNotIn(
            "'updated_at': ",
            str(BaseModel(gender='female', id='u-55'))
        )
        self.assertRegex(
            str(BaseModel()),
            r'\[BaseModel\] \([0-9a-zA-Z]+(?:-[0-9a-zA-Z]+)*\) \{.+\}'
        )
        self.assertEqual(
            str(BaseModel(id='m-345')),
            "[BaseModel] (m-345) {'id': 'm-345'}"
        )
        self.assertEqual(
            str(BaseModel(id=45)),
            "[BaseModel] (45) {'id': 45}"
        )
        self.assertEqual(
            str(BaseModel(id=None)),
            "[BaseModel] (None) {'id': None}"
        )
        with self.assertRaises(AttributeError):
            str(BaseModel(gender='female'))

    def test_save(self):
        """Tests the save function of the BaseModel class.
        """
        # Tries to rename a file and delete it
        try:
            os.rename('file.json', 'foo')
        except IOError as e:
            print(e)
        try:
            os.remove('file.json')
        except IOError as e:
            print(e)
        try:
            os.rename('foo', 'file.json')
        except IOError as e:
            print(e)
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
        self.assertIs(type(bm.to_dict()), dict)
        # Tests if to_dict contains accurate keys
        self.assertIn('id', bm.to_dict())
        self.assertIn('created_at', bm.to_dict())
        self.assertIn('updated_at', bm.to_dict())
        self.assertIn('__class__', bm.to_dict())
        # Tests if to_dict contains added attributes
        bm.author_1 = 'Bezaleel'
        bm.author_2 = 'Celestine'
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
