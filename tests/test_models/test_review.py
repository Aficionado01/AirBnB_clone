#!/usr/bin/python3
"""A unit test module for the review model.
"""
import os
import unittest
from datetime import datetime

from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Represents the test class for the Review class.
    """

    def test_init(self):
        """Tests the initialization of the Review class.
        """
        self.assertIsInstance(Review(), BaseModel)
        self.assertTrue(hasattr(Review, 'place_id'))
        self.assertTrue(hasattr(Review, 'user_id'))
        self.assertTrue(hasattr(Review, 'text'))
        self.assertIsInstance(Review.place_id, str)
        self.assertIsInstance(Review.user_id, str)
        self.assertIsInstance(Review.text, str)
        self.assertEqual(Review().place_id, '')
        self.assertEqual(Review().user_id, '')
        self.assertEqual(Review().text, '')
        self.assertEqual(Review('p-e3').place_id, '')
        self.assertEqual(Review('u-a5').user_id, '')
        self.assertEqual(Review('T\'was fun').text, '')
        self.assertEqual(Review(place_id='p-e3').place_id, 'p-e3')
        self.assertEqual(Review(user_id='u-a5').user_id, 'u-a5')
        self.assertEqual(Review(text='T\'was fun').text, 'T\'was fun')
        self.assertEqual(Review('p-e8', place_id='p-e9').place_id, 'p-e9')
        self.assertEqual(Review('u-a3', user_id='u-a2').user_id, 'u-a2')
        self.assertEqual(Review('Loved it', text='GOOD').text, 'GOOD')

    def test_str(self):
        """Tests the __str__ function of the Review class.
        """
        datetime_now = datetime.today()
        datetime_now_repr = repr(datetime_now)
        mdl = Review()
        mdl.id = '012345'
        mdl.created_at = mdl.updated_at = datetime_now
        mdl_str = str(mdl)
        self.assertIn("[Review] (012345)", mdl_str)
        self.assertIn("'id': '012345'", mdl_str)
        self.assertIn("'created_at': " + datetime_now_repr, mdl_str)
        self.assertIn("'updated_at': " + datetime_now_repr, mdl_str)
        self.assertIn("'id': ", str(Review()))
        self.assertIn("'created_at': ", str(Review()))
        self.assertIn("'updated_at': ", str(Review()))
        self.assertIn(
            "'gender': 'female'",
            str(Review(gender='female', id='m-77'))
        )
        self.assertNotIn(
            "'created_at': ",
            str(Review(gender='female', id='u-88'))
        )
        self.assertNotIn(
            "'updated_at': ",
            str(Review(gender='female', id='u-55'))
        )
        self.assertRegex(
            str(Review()),
            r'\[Review\] \([0-9a-zA-Z]+(?:-[0-9a-zA-Z]+)*\) \{.+\}'
        )
        self.assertEqual(
            str(Review(id='m-345')),
            "[Review] (m-345) {'id': 'm-345'}"
        )
        self.assertEqual(
            str(Review(id=45)),
            "[Review] (45) {'id': 45}"
        )
        self.assertEqual(
            str(Review(id=None)),
            "[Review] (None) {'id': None}"
        )
        with self.assertRaises(AttributeError):
            str(Review(gender='female'))

    def test_to_dict(self):
        """Tests the to_dict function of the Review class.
        """
        # Tests if it's a dictionary
        self.assertIsInstance(Review().to_dict(), dict)
        # Tests if to_dict contains accurate keys
        self.assertIn('id', Review().to_dict())
        self.assertIn('created_at', Review().to_dict())
        self.assertIn('updated_at', Review().to_dict())
        # Tests if to_dict contains added attributes
        mdl = Review()
        mdl.firstname = 'Celestine'
        mdl.lastname = 'Akpanoko'
        self.assertIn('firstname', mdl.to_dict())
        self.assertIn('lastname', mdl.to_dict())
        self.assertIn('firstname', Review(firstname='Celestine').to_dict())
        self.assertIn('lastname', Review(lastname='Akpanoko').to_dict())
        # Tests to_dict datetime attributes if they are strings
        self.assertIsInstance(Review().to_dict()['created_at'], str)
        self.assertIsInstance(Review().to_dict()['updated_at'], str)
        # Tests to_dict output
        datetime_now = datetime.today()
        mdl = Review()
        mdl.id = '012345'
        mdl.created_at = mdl.updated_at = datetime_now
        to_dict = {
            'id': '012345',
            '__class__': 'Review',
            'created_at': datetime_now.isoformat(),
            'updated_at': datetime_now.isoformat()
        }
        self.assertDictEqual(mdl.to_dict(), to_dict)
        self.assertDictEqual(
            Review(id='u-b34', age=13).to_dict(),
            {
                '__class__': 'Review',
                'id': 'u-b34',
                'age': 13
            }
        )
        self.assertDictEqual(
            Review(id='u-b34', age=None).to_dict(),
            {
                '__class__': 'Review',
                'id': 'u-b34',
                'age': None
            }
        )
        # Tests to_dict output contradiction
        mdl_d = Review()
        self.assertIn('__class__', Review().to_dict())
        self.assertNotIn('__class__', Review().__dict__)
        self.assertNotEqual(mdl_d.to_dict(), mdl_d.__dict__)
        self.assertNotEqual(
            mdl_d.to_dict()['__class__'],
            mdl_d.__class__
        )
        # Tests to_dict with arg
        with self.assertRaises(TypeError):
            Review().to_dict(None)
        with self.assertRaises(TypeError):
            Review().to_dict(Review())
        with self.assertRaises(TypeError):
            Review().to_dict(45)

    def tearDown(self):
        """Deconstructs this test class.
        """
        super().tearDown()
        if os.path.isfile('file.json'):
            os.unlink('file.json')
