#!/usr/bin/python3
"""A unit test module for the console (command interpreter).
"""
import json
import os
import unittest
from datetime import datetime
from io import StringIO
from typing import TextIO
from unittest.mock import patch

from console import HBNBCommand
from models import storage
# from models.base_model import BaseModel
# from models.user import User
# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.place import Place
# from models.review import Review
# from models.engine.file_storage import FileStorage
from tests import (
    # write_text_file,
    # delete_file,
    reset_store,
    clear_stream
)


class TestHBNBCommand(unittest.TestCase):
    """Represents the test class for the HBNBCommand class.
    """

    def test_console_v_0_0_1(self):
        """Tests the features of version 0.0.1 of the console.
        """
        with patch('sys.stdout', new=StringIO()) as cout:
            cons = HBNBCommand()
            # normal empty line
            cons.onecmd('')
            cons.onecmd('    ')
            self.assertEqual(cout.getvalue(), '')
            # empty line after a wrong command
            clear_stream(cout)
            cons.onecmd('ls')
            cons.onecmd('')
            cons.onecmd('  ')
            self.assertEqual(cout.getvalue(), '*** Unknown syntax: ls\n')
            # the help command
            clear_stream(cout)
            cons.onecmd('help')
            self.assertNotEqual(cout.getvalue().strip(), '')
            clear_stream(cout)
            cons.onecmd('help quit')
            self.assertNotEqual(cout.getvalue().strip(), '')

    # TODO: Write tests for this feature
    def test_console_v_0_1(self):
        """Tests the features of version 0.1 of the console.
        """
        with patch('sys.stdout', new=StringIO()) as cout:
            cons = HBNBCommand()
            if os.path.isfile('file.json'):
                os.unlink('file.json')
        # region The create command
            # missing class name
            clear_stream(cout)
            cons.onecmd('create')
            self.assertEqual(cout.getvalue(), "** class name missing **\n")
            # invalid class name
            clear_stream(cout)
            cons.onecmd('create Base')
            self.assertEqual(cout.getvalue(), "** class doesn't exist **\n")
        # endregion
        # region The show command
        # endregion
        # region The destroy command
        # endregion
        # region The all command
        # endregion
        # region The update command
        # endregion

    def test_class_count(self):
        """Tests the ClassName.count() feature.
        """
        with patch('sys.stdout', new=StringIO()) as cout:
            cons = HBNBCommand()
            reset_store(storage)
            self.assertEqual(len(storage.all()), 0)
            # no objects
            cmd_line = cons.precmd('User.count()')
            cons.onecmd(cmd_line)
            self.assertEqual(cout.getvalue(), "0\n")
            # creating objects and counting them
            cons.onecmd('create User')
            cons.onecmd('create User')
            clear_stream(cout)
            cmd_line = cons.precmd('User.count()')
            cons.onecmd(cmd_line)
            self.assertEqual(cout.getvalue(), "2\n")
            self.assertTrue(int(cout.getvalue()) >= 0)

    def test_class_destroy(self):
        """Tests the ClassName.destroy(id) feature.
        """
        with patch('sys.stdout', new=StringIO()) as cout:
            cons = HBNBCommand()
            reset_store(storage)
            # create a sample object and destroy it
            cons.onecmd('create City')
            mdl_id = cout.getvalue().strip()
            clear_stream(cout)
            cmd_line = cons.precmd(
                'City.destroy({})'.format(mdl_id)
            )
            cons.onecmd(cmd_line)
            clear_stream(cout)
            cons.onecmd('show City {}'.format(mdl_id))
            self.assertEqual(cout.getvalue(), "** no instance found **\n")

    def test_class_update_0(self):
        """Tests the ClassName.update(id, attr_name, attr_value) feature.
        """
        with patch('sys.stdout', new=StringIO()) as cout:
            cons = HBNBCommand()
            reset_store(storage)
            # create a sample object and update it
            cons.onecmd('create Place')
            mdl_id = cout.getvalue().strip()
            clear_stream(cout)
            cmd_line = cons.precmd(
                'Place.update({}, '.format(mdl_id) +
                'name, "Rio de Janeiro")'
            )
            cons.onecmd(cmd_line)
            cons.onecmd('show Place {}'.format(mdl_id))
            self.assertIn(
                "'name': 'Rio de Janeiro'",
                cout.getvalue()
            )

    def test_class_update_1(self):
        """Tests the ClassName.update(id, dict_repr) feature.
        """
        with patch('sys.stdout', new=StringIO()) as cout:
            cons = HBNBCommand()
            reset_store(storage)
            # create a sample object and update it
            cons.onecmd('create Amenity')
            mdl_id = cout.getvalue().strip()
            clear_stream(cout)
            cmd_line = cons.precmd(
                'Amenity.update({}, '.format(mdl_id) +
                "{'name': 'Basketball court'})"
            )
            cons.onecmd(cmd_line)
            cons.onecmd('show Amenity {}'.format(mdl_id))
            self.assertIn(
                "'name': 'Basketball court'",
                cout.getvalue()
            )
