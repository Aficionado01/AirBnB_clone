#!/usr/bin/python3
"""A unit test module for the console (command interpreter).
"""
import os
from typing import TextIO
import unittest
from datetime import datetime
from io import StringIO
from unittest.mock import patch

from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from tests import (
    write_text_file,
    delete_file,
    reset_store,
    clear_stream
)


class TestHBNBCommand(unittest.TestCase):
    """Represents the test class for the HBNBCommand class.
    """

    def test_emptyline(self):
        """Tests the emptyline function of the HBNBCommand class.
        """
        with patch('sys.stdout', new=StringIO()) as cout:
            cons = HBNBCommand()
            # normal empty line
            cons.onecmd('')
            cons.onecmd('    ')
            cons.onecmd('    \t\t')
            cons.onecmd('    \t  \t')
            cons.onecmd('\t   ')
            cons.onecmd('\n   ')
            cons.onecmd('   \n')
            cons.onecmd('\n   \n')
            self.assertEqual(cout.getvalue(), '')
            # empty line after a wrong command
            clear_stream(cout)
            cons.onecmd('ls')
            cons.onecmd('')
            cons.onecmd('  ')
            self.assertEqual(cout.getvalue(), '*** Unknown syntax: ls\n')

    def test_do_help(self):
        """Tests the do_help function of the HBNBCommand class.
        """
        with patch('sys.stdout', new=StringIO()) as cout:
            cons = HBNBCommand()
            reset_store(storage)
            cons.onecmd('help')
            self.assertNotEqual(cout.getvalue().strip(), '')
            clear_stream(cout)
            cons.onecmd('help create')
            self.assertNotEqual(cout.getvalue().strip(), '')

    def test_do_create(self):
        """Tests the do_create function of the HBNBCommand class.
        """
        with patch('sys.stdout', new=StringIO()) as cout:
            cons = HBNBCommand()
            reset_store(storage)
            self.assertEqual(len(storage.all()), 0)
            # with no class
            clear_stream(cout)
            cons.onecmd('create')
            self.assertEqual(cout.getvalue(), "** class name missing **\n")
            # with invalid args
            clear_stream(cout)
            cons.onecmd('create 456')
            self.assertEqual(cout.getvalue(), "** class doesn't exist **\n")
            clear_stream(cout)
            cons.onecmd('create place')
            self.assertEqual(cout.getvalue(), "** class doesn't exist **\n")
            clear_stream(cout)
            cons.onecmd('create PLACE')
            self.assertEqual(cout.getvalue(), "** class doesn't exist **\n")
            clear_stream(cout)
            cons.onecmd('create PLACE Place')
            self.assertEqual(cout.getvalue(), "** class doesn't exist **\n")
            # with valid args
            clear_stream(cout)
            cons.onecmd('create State')
            self.assertIn(
                'State.{}'.format(cout.getvalue().strip()),
                storage.all()
            )
            # with valid args (only one class is taken)
            clear_stream(cout)
            cons.onecmd('create State City')
            self.assertIn(
                'State.{}'.format(cout.getvalue().strip()),
                storage.all()
            )
            self.assertNotIn(
                'City.{}'.format(cout.getvalue().strip()),
                storage.all()
            )
            reset_store(storage)

    # def test_do_show(self):
    #     """Tests the do_show function of the HBNBCommand class.
    #     """
    #     pass

    def test_do_destroy(self):
        """Tests the do_destroy function of the HBNBCommand class.
        """
        with patch('sys.stdout', new=StringIO()) as cout:
            cons = HBNBCommand()
            reset_store(storage)
            # no arguments
            cons.onecmd('destroy')
            self.assertEqual(cout.getvalue(), "** class name missing **\n")
            # unknown class
            clear_stream(cout)
            cons.onecmd('destroy voot')
            self.assertEqual(cout.getvalue(), "** class doesn't exist **\n")
            # unknown class with valid instance id
            clear_stream(cout)
            cons.onecmd('create User')
            mdl_id = cout.getvalue().strip()
            clear_stream(cout)
            cons.onecmd('destroy voot {}'.format(mdl_id))
            self.assertEqual(cout.getvalue(), "** class doesn't exist **\n")
            self.assertIn('User.{}'.format(mdl_id), storage.all())
            # known class with no instance id
            clear_stream(cout)
            cons.onecmd('destroy User')
            self.assertEqual(cout.getvalue(), "** instance id missing **\n")
            self.assertIn('User.{}'.format(mdl_id), storage.all())
            # known class with unknown instance id
            clear_stream(cout)
            cons.onecmd('destroy User 444')
            self.assertEqual(cout.getvalue(), "** no instance found **\n")
            self.assertIn('User.{}'.format(mdl_id), storage.all())
            # unknown class with valid instance id
            clear_stream(cout)
            self.assertIn('User.{}'.format(mdl_id), storage.all())
            cons.onecmd('destroy User {}'.format(mdl_id))
            self.assertNotIn('User.{}'.format(mdl_id), storage.all())
            self.assertEqual(cout.getvalue().strip(), "")

    # def test_do_all(self):
    #     """Tests the do_all function of the HBNBCommand class.
    #     """
    #     pass

    # def test_do_update(self):
    #     """Tests the do_update function of the HBNBCommand class.
    #     """
    #     pass

    # def test_cls_all(self):
    #     """Tests the all class action of the HBNBCommand class.
    #     """
    #     pass

    def test_cls_count(self):
        """Tests the count class action of the HBNBCommand class.
        """
        with patch('sys.stdout', new=StringIO()) as cout:
            cons = HBNBCommand()
            reset_store(storage)
            self.assertEqual(len(storage.all()), 0)
            cons.precmd('User.count()')
            self.assertEqual(cout.getvalue(), "0\n")
            cons.onecmd('create User')
            cons.onecmd('create User')
            clear_stream(cout)
            cons.precmd('User.count()')
            self.assertEqual(cout.getvalue(), "2\n")
            self.assertTrue(int(cout.getvalue()) >= 0)

    # def test_cls_show(self):
    #     """Tests the show class action of the HBNBCommand class.
    #     """
    #     pass

    def test_cls_destroy(self):
        """Tests the destroy class action of the HBNBCommand class.
        """
        pass

    # def test_cls_update(self):
    #     """Tests the update class action of the HBNBCommand class.
    #     """
