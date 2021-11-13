#!/usr/bin/python3
"""A unit test module for the base model of all models.
"""
import os
import unittest
from datetime import datetime
from time import sleep

from models.base_model import BaseModel
from tests import write_text_file


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
        mdl1 = BaseModel()
        mdl2 = BaseModel()
        self.assertNotEqual(mdl1.id, mdl2.id)
        # Tests for differences in created time
        mdl3 = BaseModel()
        sleep(0.06)
        mdl4 = BaseModel()
        self.assertLess(mdl3.created_at, mdl4.created_at)
        # Tests for differences in updated time
        mdl3 = BaseModel()
        sleep(0.06)
        mdl4 = BaseModel()
        self.assertLess(mdl3.updated_at, mdl4.updated_at)
        # Tests for unused args
        mdl = BaseModel(None)
        self.assertNotIn(None, mdl.__dict__.values())
        # Tests instantiation with kwargs
        datetime_now = datetime.today()
        datetime_now_iso = datetime_now.isoformat()
        mdl = BaseModel(
            id='012',
            created_at=datetime_now_iso,
            updated_at=datetime_now_iso
        )
        self.assertEqual(mdl.id, '012')
        self.assertEqual(mdl.created_at, datetime_now)
        self.assertEqual(mdl.updated_at, datetime_now)
        # Tests instantiations with None kwargs
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)
        # Tests instantiation with args and kwargs
        datetime_now = datetime.today()
        datetime_now_iso = datetime_now.isoformat()
        mdl = BaseModel(
            '01', id='012', created_at=datetime_now_iso,
            updated_at=datetime_now_iso
        )
        self.assertEqual(mdl.id, '012')
        self.assertEqual(mdl.created_at, datetime_now)
        self.assertEqual(mdl.updated_at, datetime_now)
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
        mdl = BaseModel()
        mdl.id = '012345'
        mdl.created_at = mdl.updated_at = datetime_now
        mdl_str = str(mdl)
        self.assertIn("[BaseModel] (012345)", mdl_str)
        self.assertIn("'id': '012345'", mdl_str)
        self.assertIn("'created_at': " + datetime_now_repr, mdl_str)
        self.assertIn("'updated_at': " + datetime_now_repr, mdl_str)
        self.assertIn("'id': ", str(BaseModel()))
        self.assertIn("'created_at': ", str(BaseModel()))
        self.assertIn("'updated_at': ", str(BaseModel()))
        self.assertIn(
            "'gender': 'female'",
            str(BaseModel(gender='female', id='m-77'))
        )
        self.assertIn(
            "'id': 'm-77'",
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
        if os.path.isfile('file.json'):
            os.unlink('file.json')
        self.assertFalse(os.path.isfile('file.json'))
        mdl = BaseModel(id='this -is-a-unique-id')
        self.assertFalse(hasattr(mdl, 'updated_at'))
        mdl.save()
        self.assertTrue(hasattr(mdl, 'updated_at'))
        self.assertTrue(os.path.isfile('file.json'))
        self.assertGreater(os.stat('file.json').st_size, 15)
        with self.assertRaises(TypeError):
            BaseModel().save(mdl)
        with self.assertRaises(TypeError):
            BaseModel().save(BaseModel())
        with self.assertRaises(TypeError):
            BaseModel().save(None)
        # Tests save updates on file
        write_text_file('file.json', '{}')
        mdl = BaseModel()
        mdl.save()
        with open('file.json', 'r') as f:
            line = f.readline()
            self.assertIn('"id": ', line)
            self.assertIn('"created_at": ', line)
            self.assertIn('"updated_at": ', line)

    def test_to_dict(self):
        """Tests the to_dict function of the BaseModel class.
        """
        # Tests if it's a dictionary
        self.assertIsInstance(BaseModel().to_dict(), dict)
        # Tests if to_dict contains accurate keys
        self.assertIn('id', BaseModel().to_dict())
        self.assertIn('created_at', BaseModel().to_dict())
        self.assertIn('updated_at', BaseModel().to_dict())
        # Tests if to_dict contains added attributes
        mdl = BaseModel()
        mdl.firstname = 'Celestine'
        mdl.lastname = 'Akpanoko'
        self.assertIn('firstname', mdl.to_dict())
        self.assertIn('lastname', mdl.to_dict())
        self.assertIn('firstname', BaseModel(firstname='Celestine').to_dict())
        self.assertIn('lastname', BaseModel(lastname='Akpanoko').to_dict())
        # Tests to_dict datetime attributes if they are strings
        self.assertIsInstance(BaseModel().to_dict()['created_at'], str)
        self.assertIsInstance(BaseModel().to_dict()['updated_at'], str)
        # Tests to_dict output
        datetime_now = datetime.today()
        mdl = BaseModel()
        mdl.id = '012345'
        mdl.created_at = mdl.updated_at = datetime_now
        to_dict = {
            'id': '012345',
            '__class__': 'BaseModel',
            'created_at': datetime_now.isoformat(),
            'updated_at': datetime_now.isoformat()
        }
        self.assertDictEqual(mdl.to_dict(), to_dict)
        self.assertDictEqual(
            BaseModel(id='u-b34', age=13).to_dict(),
            {
                '__class__': 'BaseModel',
                'id': 'u-b34',
                'age': 13
            }
        )
        self.assertDictEqual(
            BaseModel(id='u-b34', age=None).to_dict(),
            {
                '__class__': 'BaseModel',
                'id': 'u-b34',
                'age': None
            }
        )
        # Tests to_dict output contradiction
        mdl_d = BaseModel()
        self.assertIn('__class__', BaseModel().to_dict())
        self.assertNotIn('__class__', BaseModel().__dict__)
        self.assertNotEqual(mdl_d.to_dict(), mdl_d.__dict__)
        self.assertNotEqual(
            mdl_d.to_dict()['__class__'],
            mdl_d.__class__
        )
        # Tests to_dict with arg
        with self.assertRaises(TypeError):
            BaseModel().to_dict(None)
        with self.assertRaises(TypeError):
            BaseModel().to_dict(BaseModel())
        with self.assertRaises(TypeError):
            BaseModel().to_dict(45)

    def tearDown(self):
        """Deconstructs this test class.
        """
        super().tearDown()
        if os.path.isfile('file.json'):
            os.unlink('file.json')
