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
