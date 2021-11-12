#!/usr/bin/python3
"""A unit test module for the file storage.
"""
import os
import unittest

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from tests import write_text_file


class TestFileStorage(unittest.TestCase):
    """Represents the test class for the FileStorage class.
    """

    def test_init(self):
        """Tests the initialization of the FileStorage class.
        """
        self.assertFalse(hasattr(FileStorage, '__file_path'))
        self.assertFalse(hasattr(FileStorage, '__objects'))

    def test_all(self):
        """Tests the all function of the FileStorage class.
        """
        write_text_file('file.json', '{}')
        store = FileStorage()
        store.reload()
        mdl = BaseModel()
        self.assertEqual(len(store.all()), 1)
        mdl = User()
        mdl = City()
        mdl = State()
        mdl = Amenity()
        mdl = Place()
        mdl = Review()
        self.assertEqual(len(store.all()), 7)
        with self.assertRaises(TypeError):
            store.all(mdl, None)
        with self.assertRaises(TypeError):
            store.all(mdl, mdl)
        with self.assertRaises(TypeError):
            store.all(None)
        with self.assertRaises(TypeError):
            store.all(store)

    def test_new(self):
        """Tests the new function of the FileStorage class.
        """
        write_text_file('file.json', '{}')
        store = FileStorage()
        store.reload()
        mdl = User(**{'id': '5'})
        store.new(mdl)
        self.assertEqual(len(store.all()), 1)
        store.new(mdl)
        store.new(mdl)
        store.new(mdl)
        self.assertEqual(len(store.all()), 1)
        with self.assertRaises(TypeError):
            store.new(mdl, None)
        with self.assertRaises(TypeError):
            store.new(mdl, mdl)
        with self.assertRaises(AttributeError):
            store.new(None)

    def test_save(self):
        """Tests the save function of the FileStorage class.
        """
        store = FileStorage()
        mdl = User(**{'id': '5'})
        store.new(mdl)
        if os.path.isfile('file.json'):
            os.unlink('file.json')
        self.assertFalse(os.path.isfile('file.json'))
        store.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertGreater(os.stat('file.json').st_size, 10)
        with self.assertRaises(TypeError):
            store.save(mdl)
        with self.assertRaises(TypeError):
            store.save(mdl, None)
        with self.assertRaises(TypeError):
            store.save(mdl, mdl)
        with self.assertRaises(TypeError):
            store.save(None)

    def test_reload(self):
        """Tests the reload function of the FileStorage class.
        """
        write_text_file('file.json', '{}')
        store = FileStorage()
        store.reload()
        self.assertEqual(len(store.all()), 0)
        if os.path.isfile('file.json'):
            os.unlink('file.json')
        self.assertFalse(os.path.isfile('file.json'))
        store.reload()
        self.assertFalse(os.path.isfile('file.json'))
        mdl = User(**{'id': '5'})
        mdl1 = City(**{'id': '7', 'name': 'Oklahoma'})
        store.new(mdl)
        store.new(mdl1)
        store.save()
        self.assertEqual(len(store.all()), 2)
        new_store = FileStorage()
        self.assertEqual(len(new_store.all()), 2)
        if os.path.isfile('file.json'):
            os.unlink('file.json')
        new_store.reload()
        self.assertEqual(len(new_store.all()), 2)
        with open('file.json', mode='w') as file:
            file.write('{}')
        new_store.reload()
        self.assertEqual(len(new_store.all()), 0)
        with self.assertRaises(TypeError):
            store.reload(mdl)
        with self.assertRaises(TypeError):
            store.reload(mdl, None)
        with self.assertRaises(TypeError):
            store.reload(mdl, mdl)
        with self.assertRaises(TypeError):
            store.reload(None)
