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
