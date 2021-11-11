#!/usr/bin/python3
"""A unit test module for the base model of all models.
"""
import unittest
from datetime import datetime
import re
import os
import time

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
        self.assertTrue(hasattr(BaseModel(), 'updated_at'))
        self.assertIsInstance(BaseModel().id, str)
        self.assertIsInstance(BaseModel().created_at, datetime)
        self.assertIsInstance(BaseModel().updated_at, datetime)
        self.assertIsInstance(BaseModel(**{
            'id': 'd211f6a0-c3aa-4261-8fa1-5be1873f2aa4',
            'created_at': '2021-11-10T12:50:06.589225',
            'updated_at': '2021-11-10T12:50:06.589242',
            'name': 'My_First_Model',
            'my_number': 89,
            '__class__': 'BaseModel'
        }).created_at, datetime)
        self.assertIsInstance(BaseModel(**{
            'id': 'd211f6a0-c3aa-4261-8fa1-5be1873f2aa4',
            'created_at': '2021-11-10T12:50:06.589225',
            'updated_at': '2021-11-10T12:50:06.589242',
            'name': 'My_First_Model',
            'my_number': 89,
            '__class__': 'BaseModel'
        }).updated_at, datetime)
        self.assertEqual(BaseModel(**{
            'id': None,
            'created_at': '2021-11-10T12:50:06.589225',
            'updated_at': '2021-11-10T12:50:06.589242',
            'name': 'My_First_Model',
            'my_number': 89,
            '__class__': 'BaseModel'
        }).id, None)
        remove_files()
        self.assertEqual(BaseModel(**{
            'id': 'd211f6a0-c3aa-4261-8fa1-5be1873f2aa4',
            'created_at': '2021-11-10T12:50:06.589225',
            'updated_at': '2021-11-10T12:50:06.589242',
            'name': 'My_First_Model',
            'my_number': 89,
            '__class__': 'BaseModel'
        }).id, 'd211f6a0-c3aa-4261-8fa1-5be1873f2aa4')
        self.assertEqual(BaseModel(**{
            'id': 'd211f6a0-c3aa-4261-8fa1-5be1873f2aa4',
            'created_at': '2021-11-10T12:50:06.589225',
            'updated_at': '2021-11-10T12:50:06.589242',
            'name': 'My_First_Model',
            'my_number': 89,
            '__class__': 'BaseModel'
        }).name, 'My_First_Model')
        self.assertEqual(BaseModel(**{
            'id': 'd211f6a0-c3aa-4261-8fa1-5be1873f2aa4',
            'created_at': '2021-11-10T12:50:06.589225',
            'updated_at': '2021-11-10T12:50:06.589242',
            'name': 'My_First_Model',
            'my_number': 89,
            '__class__': 'BaseModel'
        }).my_number, 89)
        self.assertNotEqual(BaseModel(**{
            'id': 'd211f6a0-c3aa-4261-8fa1-5be1873f2aa4',
            'created_at': '2021-11-10T12:50:06.589225',
            'updated_at': '2021-11-10T12:50:06.589242',
            'name': 'My_First_Model',
            'my_number': 89,
            '__class__': '777888'
        }).__class__, '777888')
        self.assertEqual(BaseModel(**{
            'id': 'd211f6a0-c3aa-4261-8fa1-5be1873f2aa4',
            'created_at': '2021-11-10T12:50:06.589225',
            'updated_at': '2021-11-10T12:50:06.589242',
            'name': 'My_First_Model',
            'my_number': 89,
            '__class__': None
        }).__class__.__name__, 'BaseModel')
        self.assertEqual(BaseModel(**{
            'id': 'd211f6a0-c3aa-4261-8fa1-5be1873f2aa4',
            'created_at': '2021-11-10T12:50:06.589225',
            'updated_at': '2021-11-10T12:50:06.589242',
            'name': 'My_First_Model',
            'my_number': 89,
            '__class__': 'User'
        }).__class__.__name__, 'BaseModel')
        self.assertEqual(BaseModel(**{
            'id': 'd211f6a0-c3aa-4261-8fa1-5be1873f2aa4',
            'created_at': '2021-11-10T12:50:06.589225',
            'updated_at': '2021-11-10T12:50:06.589242',
            'name': 'My_First_Model',
            'my_number': 89,
            '__class__': 'BaseModel'
        }).created_at, datetime(2021, 11, 10, 12, 50, 6, 589225))
        self.assertEqual(BaseModel(**{
            'id': 'd211f6a0-c3aa-4261-8fa1-5be1873f2aa4',
            'created_at': '2021-11-10T12:50:06.589225',
            'updated_at': '2021-11-10T12:50:06.589242',
            'name': 'My_First_Model',
            'my_number': 89,
            '__class__': 'BaseModel'
        }).updated_at, datetime(2021, 11, 10, 12, 50, 6, 589242))
        self.assertNotEqual(BaseModel().id, BaseModel().id)

    def test_save(self):
        """Tests the save function of the BaseModel class.
        """
        pass
        # dummy = self.dummy
        # time.sleep(1)
        # dummy.save()
        # self.assertGreater(dummy.updated_at, dummy.created_at)

    def test_to_dict(self):
        """Tests the to_dict function of the BaseModel class.
        """
        pass
