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

    def test_do_create(self):
        """Tests the do_create function of the HBNBCommand class.
        """
        delete_file('file.json')
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
