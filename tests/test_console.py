#!/usr/bin/python3
"""A unit test module for the console (command interpreter).
"""
import json
import os
import unittest
from io import StringIO
from unittest.mock import patch

from console import HBNBCommand
from tests import remove_files


class TestHBNBCommand(unittest.TestCase):
    """Represents the test class for the HBNBCommand class.
    """

    def test_prompt(self):
        """Tests the prompt attribute of the HBNBCommand class.
        """
        self.assertEqual(HBNBCommand().prompt.strip(), '(hbnb)')

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

    def test_do_help(self):
        """Tests the do_help function of the HBNBCommand class.
        """
        min_doc_size = 20
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('help')
            self.assertTrue(len(istdout.getvalue()) >= min_doc_size)
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('help quit')
            self.assertTrue(len(istdout.getvalue()) >= min_doc_size)
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('help quit 78')
            self.assertTrue(len(istdout.getvalue()) >= min_doc_size)
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('help 78')
            self.assertEqual(istdout.getvalue(), "*** No help on 78\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('help 78 quit')
            self.assertEqual(istdout.getvalue(), "*** No help on 78 quit\n")

    def test_do_create(self):
        """Tests the do_create function of the HBNBCommand class.
        """
        remove_files()
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('create 78')
            self.assertEqual(istdout.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('create 78 User')
            self.assertEqual(istdout.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('create Place')
            self.assertRegex(istdout.getvalue(), r'[0-9a-zA-Z]+(-[0-9a-zA-Z]+)*\n')

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

    def test_class_action(self):
        """Tests the class action syntax of the HBNBCommand class.
        """
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().precmd('foo.a')
            self.assertEqual(istdout.getvalue(), "*** Unknown syntax: foo.a\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().precmd('User.a')
            self.assertEqual(istdout.getvalue(), "*** Unknown syntax: User.a\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().precmd('User.all')
            self.assertEqual(istdout.getvalue(), "*** Unknown syntax: User.all\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().precmd('User.all(')
            self.assertEqual(istdout.getvalue(), "*** Unknown syntax: User.all(\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().precmd('User.all)')
            self.assertEqual(istdout.getvalue(), "*** Unknown syntax: User.all)\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().precmd('User.all(")')
            self.assertEqual(istdout.getvalue(), "*** Unknown syntax: User.all(\")\n")
        # with patch('sys.stdout', new=StringIO()) as istdout:
        #     HBNBCommand().precmd('User.all(1 23)')
        #     self.assertEqual(istdout.getvalue(), "*** Unknown syntax: User.all(1 23)\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().precmd('User.foo()')
            self.assertEqual(istdout.getvalue(), "*** Unknown syntax: User.foo()\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().precmd('.all()')
            self.assertEqual(istdout.getvalue(), "*** Unknown syntax: .all()\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().precmd('User.()')
            self.assertEqual(istdout.getvalue(), "*** Unknown syntax: User.()\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().precmd('User()')
            self.assertEqual(istdout.getvalue(), "*** Unknown syntax: User()\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().precmd('User.show "49faff9a-6318-451f-87b6-910505c55907"')
            self.assertEqual(
                istdout.getvalue(),
                '*** Unknown syntax: User.show "49faff9a-6318-451f-87b6-910505c55907"\n'
            )
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().precmd('foo.all()')
            self.assertEqual(istdout.getvalue(), "** class doesn't exist **\n")
