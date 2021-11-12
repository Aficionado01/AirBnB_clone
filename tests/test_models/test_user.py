#!/usr/bin/python3
"""A unit test module for the user model.
"""
import unittest
from datetime import datetime

from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Represents the test class for the User class.
    """

    def test_init(self):
        """Tests the initialization of the User class.
        """
        self.assertIsInstance(User(), BaseModel)
        self.assertTrue(hasattr(User, 'first_name'))
        self.assertTrue(hasattr(User, 'last_name'))
        self.assertTrue(hasattr(User, 'email'))
        self.assertTrue(hasattr(User, 'password'))
        self.assertIsInstance(User.first_name, str)
        self.assertIsInstance(User.last_name, str)
        self.assertIsInstance(User.email, str)
        self.assertIsInstance(User.password, str)
        self.assertEqual(User().first_name, '')
        self.assertEqual(User().last_name, '')
        self.assertEqual(User().email, '')
        self.assertEqual(User().password, '')
        self.assertEqual(User('Dave').first_name, '')
        self.assertEqual(User('Pink').last_name, '')
        self.assertEqual(User('4@tmail.com').email, '')
        self.assertEqual(User('password123').password, '')
        self.assertEqual(User(first_name='Lily').first_name, 'Lily')
        self.assertEqual(User(last_name='Robben').last_name, 'Robben')
        self.assertEqual(User(email='llr@tmail.com').email, 'llr@tmail.com')
        self.assertEqual(User(password='12345').password, '12345')
        self.assertEqual(User('Robin', first_name='Nami').first_name, 'Nami')
        self.assertEqual(User('Eck', last_name='Castro').last_name, 'Castro')
        self.assertEqual(User('mo', email='n@rmail.com').email, 'n@rmail.com')
        self.assertEqual(User('12345', password='Nami').password, 'Nami')
