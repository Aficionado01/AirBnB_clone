#!/usr/bin/python3
"""A unit test module for the console (command interpreter).
"""
import json
import os
import unittest
from io import StringIO
from unittest.mock import patch

from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Represents the test class for the HBNBCommand class.
    """

    def test_do_all(self):
        """Tests the do_all function of the HBNBCommand class.
        """
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('all 78')
            self.assertEqual(istdout.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('all 78 User')
            self.assertEqual(istdout.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('all Place')
            self.assertEqual(istdout.getvalue(), "[]\n")

    def test_do_EOF(self):
        """Tests the do_EOF function of the HBNBCommand class.
        """
        with self.assertRaises(SystemExit) as ex:
            with patch('sys.stdout', new=StringIO()):
                HBNBCommand().onecmd('EOF')
        self.assertEqual(ex.exception.code, 0)
        with self.assertRaises(SystemExit) as ex:
            with patch('sys.stdout', new=StringIO()):
                HBNBCommand().onecmd('all 78 User')
                HBNBCommand().onecmd('EOF')
        self.assertEqual(ex.exception.code, 0)
        with self.assertRaises(SystemExit) as ex:
            with patch('sys.stdout', new=StringIO()):
                HBNBCommand().onecmd('help')
                HBNBCommand().onecmd('    EOF')
        self.assertEqual(ex.exception.code, 0)
        with self.assertRaises(SystemExit) as ex:
            with patch('sys.stdout', new=StringIO()):
                HBNBCommand().onecmd('help')
                HBNBCommand().onecmd('    \tEOF')
        self.assertEqual(ex.exception.code, 0)

    def test_do_quit(self):
        """Tests the do_quit function of the HBNBCommand class.
        """
        with self.assertRaises(SystemExit) as ex:
            with patch('sys.stdout', new=StringIO()):
                HBNBCommand().onecmd('quit')
        self.assertEqual(ex.exception.code, 0)
        with self.assertRaises(SystemExit) as ex:
            with patch('sys.stdout', new=StringIO()):
                HBNBCommand().onecmd('all 78 User')
                HBNBCommand().onecmd('quit')
        self.assertEqual(ex.exception.code, 0)
        with self.assertRaises(SystemExit) as ex:
            with patch('sys.stdout', new=StringIO()):
                HBNBCommand().onecmd('help')
                HBNBCommand().onecmd('    quit')
        self.assertEqual(ex.exception.code, 0)
        with self.assertRaises(SystemExit) as ex:
            with patch('sys.stdout', new=StringIO()):
                HBNBCommand().onecmd('help')
                HBNBCommand().onecmd('    \tquit')
        self.assertEqual(ex.exception.code, 0)
        with self.assertRaises(SystemExit) as ex:
            with patch('sys.stdout', new=StringIO()):
                HBNBCommand().onecmd('help')
                HBNBCommand().onecmd('quit 5')
        self.assertEqual(ex.exception.code, 0)
        with self.assertRaises(SystemExit) as ex:
            with patch('sys.stdout', new=StringIO()):
                HBNBCommand().onecmd('help')
                HBNBCommand().onecmd('quit foo')
        self.assertEqual(ex.exception.code, 0)
        with self.assertRaises(SystemExit) as ex:
            with patch('sys.stdout', new=StringIO()):
                HBNBCommand().onecmd('6788_uuhjj')
                HBNBCommand().onecmd('quit')
        self.assertEqual(ex.exception.code, 0)

    def test_emptyline(self):
        """Tests the emptyline function of the HBNBCommand class.
        """
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('')
            HBNBCommand().onecmd('    ')
            HBNBCommand().onecmd('    \t\t')
            HBNBCommand().onecmd('    \t  \t')
            HBNBCommand().onecmd('\t   ')
            HBNBCommand().onecmd('\n   ')
            HBNBCommand().onecmd('   \n')
            HBNBCommand().onecmd('\n   \n')
            self.assertEqual(istdout.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as istdout:
            cons = HBNBCommand()
            cons.onecmd('ls')
            cons.onecmd('')
            cons.onecmd('')
            self.assertEqual(istdout.getvalue(), '*** Unknown syntax: ls\n')
