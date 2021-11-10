#!/usr/bin/python3
"""A unit test module for the base model of all models.
"""
import unittest
from datetime import datetime
import re
import os
import time

from models.base_model import BaseModel


class BaseModel_test(unittest.TestCase):
    """BaseModel Test Class
    """
    @classmethod
    def setUpClass(cls):
        """class setup
        """
        cls.dummy = BaseModel()

    @classmethod
    def tearDownClass(cls):
        """tear down class
        """
        del cls.dummy
        try:
            os.remove('file.json')
        except OSError:
            pass

    def test_id(self):
        """test id is a valid UUID
        """
        dummy = self.dummy
        self.assertIsInstance(dummy, BaseModel)
        self.assertIsInstance(dummy.id, str)
        is_match = re.fullmatch(r'\w{8}-\w{4}-\w{4}-\w{12}', dummy.id)
        self.assertTrue(is_match)

    def test_unique_id(self):
        """unique ID's test
        """
        dummy_1 = BaseModel()
        dummy_2 = BaseModel()
        self.assertNotEqual(dummy_1.id, dummy_2.id)
        del dummy_1
        del dummy_2

    def test_time_creation(self):
        """test the time of creation and updation
        """
        dummy = self.dummy
        self.assertIsInstance(dummy.created_at, datetime)
        self.assertIsInstance(dummy.updated_at, datetime)
        self.assertEqual(dummy.created_at, dummy.updated_at)

    def test_str(self):
        """test the string of an object
        """
        dummy = self.dummy
        result = '[{}] ({}) {}'.format('BaseModel', dummy.id, dummy.__dict__)
        self.assertEqual(str(dummy), result)

    def test_save(self):
        """test updation time after updating
        """
        dummy = self.dummy
        time.sleep(1)
        dummy.save()
        self.assertGreater(dummy.updated_at, dummy.created_at)

    def test_dict(self):
        """test dictionary representation of a model
        """
        dummy = self.dummy
        test_dict = dummy.to_dict()
        self.assertTrue('__class__' in test_dict)
        self.assertIsInstance(test_dict['__class__'], str)
        self.assertTrue('id' in test_dict)
        self.assertIsInstance(test_dict["id"], str)
        self.assertTrue('created_at' in test_dict)
        self.assertIsInstance(test_dict['created_at'], str)
        self.assertTrue('updated_at' in test_dict)
        self.assertIsInstance(test_dict['updated_at'], str)
        dummy.test = 10
        test_dict = dummy.to_dict()
        self.assertTrue('test' in test_dict)
        dummy.save()

    def test_from_dict(self):
        """test instance retrival from a dictionary
        """
        dummy = self.dummy
        dummy.test = 10
        test_instance = BaseModel(**dummy.to_dict())
        self.assertTrue('__class__' not in test_instance.__dict__)
        self.assertTrue(hasattr(test_instance, 'id'))
        self.assertTrue(hasattr(test_instance, 'created_at'))
        self.assertTrue(hasattr(test_instance, 'updated_at'))
        self.assertTrue(hasattr(test_instance, 'test'))
        self.assertEqual(test_instance.id, dummy.id)
        self.assertIsInstance(test_instance.created_at, datetime)
        self.assertIsInstance(test_instance.updated_at, datetime)
        self.assertEqual(test_instance.created_at, dummy.created_at)
        self.assertEqual(test_instance.updated_at, dummy.updated_at)


if __name__ == '__main__':
    unittest.main()
