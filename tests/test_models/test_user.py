#!/usr/bin/python3
"""A unit test module for the user model.
"""
import os
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

    def test_str(self):
        """Tests the __str__ function of the User class.
        """
        datetime_now = datetime.today()
        datetime_now_repr = repr(datetime_now)
        mdl = User()
        mdl.id = '012345'
        mdl.created_at = mdl.updated_at = datetime_now
        mdl_str = str(mdl)
        self.assertIn("[User] (012345)", mdl_str)
        self.assertIn("'id': '012345'", mdl_str)
        self.assertIn("'created_at': " + datetime_now_repr, mdl_str)
        self.assertIn("'updated_at': " + datetime_now_repr, mdl_str)
        self.assertIn("'id': ", str(User()))
        self.assertIn("'created_at': ", str(User()))
        self.assertIn("'updated_at': ", str(User()))
        self.assertIn(
            "'gender': 'female'",
            str(User(gender='female', id='m-77'))
        )
        self.assertNotIn(
            "'created_at': ",
            str(User(gender='female', id='u-88'))
        )
        self.assertNotIn(
            "'updated_at': ",
            str(User(gender='female', id='u-55'))
        )
        self.assertRegex(
            str(User()),
            r'\[User\] \([0-9a-zA-Z]+(?:-[0-9a-zA-Z]+)*\) \{.+\}'
        )
        self.assertEqual(
            str(User(id='m-345')),
            "[User] (m-345) {'id': 'm-345'}"
        )
        self.assertEqual(
            str(User(id=45)),
            "[User] (45) {'id': 45}"
        )
        self.assertEqual(
            str(User(id=None)),
            "[User] (None) {'id': None}"
        )
        with self.assertRaises(AttributeError):
            str(User(gender='female'))

    def test_to_dict(self):
        """Tests the to_dict function of the User class.
        """
        # Tests if it's a dictionary
        self.assertIsInstance(User().to_dict(), dict)
        # Tests if to_dict contains accurate keys
        self.assertIn('id', User().to_dict())
        self.assertIn('created_at', User().to_dict())
        self.assertIn('updated_at', User().to_dict())
        # Tests if to_dict contains added attributes
        mdl = User()
        mdl.firstname = 'Celestine'
        mdl.lastname = 'Akpanoko'
        self.assertIn('firstname', mdl.to_dict())
        self.assertIn('lastname', mdl.to_dict())
        self.assertIn('firstname', User(firstname='Celestine').to_dict())
        self.assertIn('lastname', User(lastname='Akpanoko').to_dict())
        # Tests to_dict datetime attributes if they are strings
        self.assertIsInstance(User().to_dict()['created_at'], str)
        self.assertIsInstance(User().to_dict()['updated_at'], str)
        # Tests to_dict output
        datetime_now = datetime.today()
        mdl = User()
        mdl.id = '012345'
        mdl.created_at = mdl.updated_at = datetime_now
        to_dict = {
            'id': '012345',
            '__class__': 'User',
            'created_at': datetime_now.isoformat(),
            'updated_at': datetime_now.isoformat()
        }
        self.assertDictEqual(mdl.to_dict(), to_dict)
        self.assertDictEqual(
            User(id='u-b34', age=13).to_dict(),
            {
                '__class__': 'User',
                'id': 'u-b34',
                'age': 13
            }
        )
        self.assertDictEqual(
            User(id='u-b34', age=None).to_dict(),
            {
                '__class__': 'User',
                'id': 'u-b34',
                'age': None
            }
        )
        # Tests to_dict output contradiction
        mdl_d = User()
        self.assertIn('__class__', User().to_dict())
        self.assertNotIn('__class__', User().__dict__)
        self.assertNotEqual(mdl_d.to_dict(), mdl_d.__dict__)
        self.assertNotEqual(
            mdl_d.to_dict()['__class__'],
            mdl_d.__class__
        )
        # Tests to_dict with arg
        with self.assertRaises(TypeError):
            User().to_dict(None)
        with self.assertRaises(TypeError):
            User().to_dict(User())
        with self.assertRaises(TypeError):
            User().to_dict(45)

    def tearDown(self):
        """Deconstructs this test class.
        """
        super().tearDown()
        if os.path.isfile('file.json'):
            os.unlink('file.json')
