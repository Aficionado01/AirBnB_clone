#!/usr/bin/python3
"""A unit test module for the base model of all models.
"""
import unittest
from datetime import datetime
import re
import os
import time
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Represents the test class for the BaseModel class.
    """

    def test_init(self):
        """Tests the initialization of the Base class.
        """
        self.assertIsInstance(BaseModel().id, str)
        self.assertIsInstance(BaseModel().created_at, datetime)
        self.assertIsInstance(BaseModel().updated_at, datetime)

    def test_save(self):
        """test updation time after updating
        """
        pass
        # dummy = self.dummy
        # time.sleep(1)
        # dummy.save()
        # self.assertGreater(dummy.updated_at, dummy.created_at)

    def test_dict(self):
        """test dictionary representation of a model
        """
        pass
        # dummy = self.dummy
        # test_dict = dummy.to_dict()
        # self.assertTrue('__class__' in test_dict)
        # self.assertIsInstance(test_dict['__class__'], str)
        # self.assertTrue('id' in test_dict)
        # self.assertIsInstance(test_dict["id"], str)
        # self.assertTrue('created_at' in test_dict)
        # self.assertIsInstance(test_dict['created_at'], str)
        # self.assertTrue('updated_at' in test_dict)
        # self.assertIsInstance(test_dict['updated_at'], str)
        # dummy.test = 10
        # test_dict = dummy.to_dict()
        # self.assertTrue('test' in test_dict)
        # dummy.save()

    def test_from_dict(self):
        """test instance retrival from a dictionary
        """
        pass
        # dummy = self.dummy
        # dummy.test = 10
        # test_instance = BaseModel(**dummy.to_dict())
        # self.assertTrue('__class__' not in test_instance.__dict__)
        # self.assertTrue(hasattr(test_instance, 'id'))
        # self.assertTrue(hasattr(test_instance, 'created_at'))
        # self.assertTrue(hasattr(test_instance, 'updated_at'))
        # self.assertTrue(hasattr(test_instance, 'test'))
        # self.assertEqual(test_instance.id, dummy.id)
        # self.assertIsInstance(test_instance.created_at, datetime)
        # self.assertIsInstance(test_instance.updated_at, datetime)
        # self.assertEqual(test_instance.created_at, dummy.created_at)
        # self.assertEqual(test_instance.updated_at, dummy.updated_at)
