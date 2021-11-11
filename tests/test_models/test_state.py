#!/usr/bin/python3
"""A unit test module for the state model.
"""
from datetime import datetime
import unittest

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
        self.assertEqual(State(name='California').name, 'California')
        self.assertEqual(State('Texas', name='Lagos').name, 'Lagos')
