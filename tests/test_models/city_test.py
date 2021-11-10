#!/usr/bin/python3
"""city testcase
"""

from models.city import City
from models.state import State
from models.base_model import BaseModel
import unittest


class CityTest(unittest.TestCase):
    """test for city class
    """
    @classmethod
    def setUpClass(cls):
        """setup
        """
        cls.dummy_city = City()
        cls.dummy_city.name = "test"
        cls.dummy_city.state_id = State().id

    @classmethod
    def tearDownClass(cls):
        """tear down
        """
        del cls.dummy_city

    def test_inheritance(self):
        """test inheritance
        """
        self.assertIsInstance(self.dummy_city, BaseModel)
        self.assertTrue(hasattr(self.dummy_city, "id"))
        self.assertTrue(hasattr(self.dummy_city, "created_at"))
        self.assertTrue(hasattr(self.dummy_city, "updated_at"))

    def test_attributes(self):
        """test attributes
        """
        self.assertTrue(hasattr(self.dummy_city, "name"))
        self.assertTrue(hasattr(self.dummy_city, "state_id"))

if __name__ == "__main__":
    unittest.main()
