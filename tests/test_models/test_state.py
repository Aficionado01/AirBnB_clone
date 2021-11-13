#!/usr/bin/python3
"""A unit test module for the state model.
"""
import os
import unittest
from datetime import datetime

from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Represents the test class for the State class.
    """

    def test_init(self):
        """Tests the initialization of the State class.
        """
        self.assertIsInstance(State(), BaseModel)
        self.assertTrue(hasattr(State, 'name'))
        self.assertIsInstance(State.name, str)
        self.assertEqual(State().name, '')
        self.assertEqual(State('Kansas').name, '')
        self.assertEqual(State(name='California').name, 'California')
        self.assertEqual(State('Texas', name='Lagos').name, 'Lagos')

    def test_str(self):
        """Tests the __str__ function of the State class.
        """
        datetime_now = datetime.today()
        datetime_now_repr = repr(datetime_now)
        mdl = State()
        mdl.id = '012345'
        mdl.created_at = mdl.updated_at = datetime_now
        mdl_str = str(mdl)
        self.assertIn("[State] (012345)", mdl_str)
        self.assertIn("'id': '012345'", mdl_str)
        self.assertIn("'created_at': " + datetime_now_repr, mdl_str)
        self.assertIn("'updated_at': " + datetime_now_repr, mdl_str)
        self.assertIn("'id': ", str(State()))
        self.assertIn("'created_at': ", str(State()))
        self.assertIn("'updated_at': ", str(State()))
        self.assertIn(
            "'gender': 'female'",
            str(State(gender='female', id='m-77'))
        )
        self.assertNotIn(
            "'created_at': ",
            str(State(gender='female', id='u-88'))
        )
        self.assertNotIn(
            "'updated_at': ",
            str(State(gender='female', id='u-55'))
        )
        self.assertRegex(
            str(State()),
            r'\[State\] \([0-9a-zA-Z]+(?:-[0-9a-zA-Z]+)*\) \{.+\}'
        )
        self.assertEqual(
            str(State(id='m-345')),
            "[State] (m-345) {'id': 'm-345'}"
        )
        self.assertEqual(
            str(State(id=45)),
            "[State] (45) {'id': 45}"
        )
        self.assertEqual(
            str(State(id=None)),
            "[State] (None) {'id': None}"
        )
        with self.assertRaises(AttributeError):
            str(State(gender='female'))

    def test_to_dict(self):
        """Tests the to_dict function of the State class.
        """
        # Tests if it's a dictionary
        self.assertIsInstance(State().to_dict(), dict)
        # Tests if to_dict contains accurate keys
        self.assertIn('id', State().to_dict())
        self.assertIn('created_at', State().to_dict())
        self.assertIn('updated_at', State().to_dict())
        # Tests if to_dict contains added attributes
        mdl = State()
        mdl.firstname = 'Celestine'
        mdl.lastname = 'Akpanoko'
        self.assertIn('firstname', mdl.to_dict())
        self.assertIn('lastname', mdl.to_dict())
        self.assertIn('firstname', State(firstname='Celestine').to_dict())
        self.assertIn('lastname', State(lastname='Akpanoko').to_dict())
        # Tests to_dict datetime attributes if they are strings
        self.assertIsInstance(State().to_dict()['created_at'], str)
        self.assertIsInstance(State().to_dict()['updated_at'], str)
        # Tests to_dict output
        datetime_now = datetime.today()
        mdl = State()
        mdl.id = '012345'
        mdl.created_at = mdl.updated_at = datetime_now
        to_dict = {
            'id': '012345',
            '__class__': 'State',
            'created_at': datetime_now.isoformat(),
            'updated_at': datetime_now.isoformat()
        }
        self.assertDictEqual(mdl.to_dict(), to_dict)
        self.assertDictEqual(
            State(id='u-b34', age=13).to_dict(),
            {
                '__class__': 'State',
                'id': 'u-b34',
                'age': 13
            }
        )
        self.assertDictEqual(
            State(id='u-b34', age=None).to_dict(),
            {
                '__class__': 'State',
                'id': 'u-b34',
                'age': None
            }
        )
        # Tests to_dict output contradiction
        mdl_d = State()
        self.assertIn('__class__', State().to_dict())
        self.assertNotIn('__class__', State().__dict__)
        self.assertNotEqual(mdl_d.to_dict(), mdl_d.__dict__)
        self.assertNotEqual(
            mdl_d.to_dict()['__class__'],
            mdl_d.__class__
        )
        # Tests to_dict with arg
        with self.assertRaises(TypeError):
            State().to_dict(None)
        with self.assertRaises(TypeError):
            State().to_dict(State())
        with self.assertRaises(TypeError):
            State().to_dict(45)

    def tearDown(self):
        """Deconstructs this test class.
        """
        super().tearDown()
        if os.path.isfile('file.json'):
            os.unlink('file.json')
