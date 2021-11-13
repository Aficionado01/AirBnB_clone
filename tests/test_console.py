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
from tests import write_text_file


def clear_stream(stream: TextIO):
    """Clears the contents of a given stream

    Args:
        stream (TextIO): The stream to clear.
    """
    if stream.seekable():
        stream.seek(0)
        stream.truncate(0)


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

    def test_do_EOF(self):
        """Tests the do_EOF function of the HBNBCommand class.
        """
        # running a single EOF
        with self.assertRaises(SystemExit) as ex:
            with patch('sys.stdout', new=StringIO()):
                HBNBCommand().onecmd('EOF')
        self.assertEqual(ex.exception.code, 0)
        # running EOF after running other commands
        with self.assertRaises(SystemExit) as ex:
            with patch('sys.stdout', new=StringIO()) as cout:
                cons = HBNBCommand()
                cons.onecmd('all 78 User')
                cons.onecmd('EOF')
        self.assertEqual(cout.getvalue(), "** class doesn't exist **\n")
        self.assertEqual(ex.exception.code, 0)
        with self.assertRaises(SystemExit) as ex:
            with patch('sys.stdout', new=StringIO()) as cout:
                cons = HBNBCommand()
                cons.onecmd('show')
                cons.onecmd('    EOF')
        self.assertEqual(cout.getvalue(), "** class name missing **\n")
        self.assertEqual(ex.exception.code, 0)
        # running commands after running EOF
        with self.assertRaises(SystemExit) as ex:
            with patch('sys.stdout', new=StringIO()):
                HBNBCommand().onecmd('    \tEOF\nhelp')
        self.assertEqual(ex.exception.code, 0)
        # running EOF with arguments
        with self.assertRaises(SystemExit) as ex:
            with patch('sys.stdout', new=StringIO()):
                HBNBCommand().onecmd('EOF 5')
        self.assertEqual(ex.exception.code, 0)

    def test_do_quit(self):
        """Tests the do_quit function of the HBNBCommand class.
        """
        # running a single quit
        with self.assertRaises(SystemExit) as ex:
            with patch('sys.stdout', new=StringIO()):
                HBNBCommand().onecmd('quit')
        self.assertEqual(ex.exception.code, 0)
        # running EOF after running other commands
        with self.assertRaises(SystemExit) as ex:
            with patch('sys.stdout', new=StringIO()) as cout:
                cons = HBNBCommand()
                cons.onecmd('all 78 User')
                cons.onecmd('quit')
        self.assertEqual(cout.getvalue(), "** class doesn't exist **\n")
        self.assertEqual(ex.exception.code, 0)
        with self.assertRaises(SystemExit) as ex:
            with patch('sys.stdout', new=StringIO()) as cout:
                cons = HBNBCommand()
                cons.onecmd('show')
                cons.onecmd('    quit')
        self.assertEqual(cout.getvalue(), "** class name missing **\n")
        self.assertEqual(ex.exception.code, 0)
        # running commands after running quit
        with self.assertRaises(SystemExit) as ex:
            with patch('sys.stdout', new=StringIO()):
                HBNBCommand().onecmd('    \tquit\nhelp')
        self.assertEqual(ex.exception.code, 0)
        # running quit with arguments
        with self.assertRaises(SystemExit) as ex:
            with patch('sys.stdout', new=StringIO()):
                HBNBCommand().onecmd('quit 5')
        self.assertEqual(ex.exception.code, 0)
