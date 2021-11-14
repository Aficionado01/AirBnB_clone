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
        with patch('sys.stdout', new=StringIO()) as cout:
            cons = HBNBCommand()
            reset_store(storage)
            # no arguments
            with self.assertRaises(SystemExit) as ex:
                cons.onecmd('EOF')
            self.assertEqual(cout.getvalue().strip(), '')
            self.assertEqual(ex.exception.code, 0)
            # arguments
            clear_stream(cout)
            with self.assertRaises(SystemExit) as ex:
                cons.onecmd('EOF 5')
            self.assertEqual(cout.getvalue().strip(), '')
            self.assertEqual(ex.exception.code, 0)
            # commands before EOF
            clear_stream(cout)
            with self.assertRaises(SystemExit) as ex:
                cons.onecmd('ls')
                cons.onecmd('EOF')
            self.assertEqual(cout.getvalue(), '*** Unknown syntax: ls\n')
            self.assertEqual(ex.exception.code, 0)
            # commands after EOF
            clear_stream(cout)
            with self.assertRaises(SystemExit) as ex:
                cons.onecmd('EOF')
                cons.onecmd('ls')
            self.assertEqual(cout.getvalue().strip(), '')
            self.assertEqual(cons.lastcmd, '')
            self.assertEqual(ex.exception.code, 0)

    def test_do_all(self):
        """Tests the do_all function of the HBNBCommand class.
        """
        with patch('sys.stdout', new=StringIO()) as cout:
            cons = HBNBCommand()
            reset_store(storage)
            # no arguments
            cons.onecmd('create Amenity')
            mdl_id = cout.getvalue().strip()
            clear_stream(cout)
            cons.onecmd('all')
            self.assertIn('[Amenity] ({})'.format(mdl_id), cout.getvalue())
            # valid class argument
            cons.onecmd('create State')
            mdl1_id = cout.getvalue().strip()
            clear_stream(cout)
            cons.onecmd('all Amenity')
            self.assertIn('[Amenity] ({})'.format(mdl_id), cout.getvalue())
            self.assertNotIn('[State] ({})'.format(mdl1_id), cout.getvalue())
            # unknowm class argument
            clear_stream(cout)
            cons.onecmd('all fgkl')
            self.assertEqual(cout.getvalue(), "** class doesn't exist **\n")

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
            # known class with valid instance id
            clear_stream(cout)
            self.assertIn('User.{}'.format(mdl_id), storage.all())
            cons.onecmd('destroy User {}'.format(mdl_id))
            self.assertNotIn('User.{}'.format(mdl_id), storage.all())
            self.assertEqual(cout.getvalue().strip(), "")

    def test_do_help(self):
        """Tests the do_help function of the HBNBCommand class.
        """
        with patch('sys.stdout', new=StringIO()) as cout:
            cons = HBNBCommand()
            reset_store(storage)
            cons.onecmd('help')
            self.assertNotEqual(cout.getvalue().strip(), '')
            # the help commands aren't empty
            clear_stream(cout)
            cons.onecmd('help create')
            self.assertNotEqual(cout.getvalue().strip(), '')
            clear_stream(cout)
            cons.onecmd('help quit')
            self.assertNotEqual(cout.getvalue().strip(), '')
            clear_stream(cout)
            cons.onecmd('help all')
            self.assertNotEqual(cout.getvalue().strip(), '')
            clear_stream(cout)
            cons.onecmd('help show')
            self.assertNotEqual(cout.getvalue().strip(), '')

    def test_do_quit(self):
        """Tests the do_quit function of the HBNBCommand class.
        """
        with patch('sys.stdout', new=StringIO()) as cout:
            cons = HBNBCommand()
            reset_store(storage)
            # no arguments
            with self.assertRaises(SystemExit) as ex:
                cons.onecmd('quit')
            self.assertEqual(cout.getvalue().strip(), '')
            self.assertEqual(ex.exception.code, 0)
            # arguments
            clear_stream(cout)
            with self.assertRaises(SystemExit) as ex:
                cons.onecmd('quit 5')
            self.assertEqual(cout.getvalue().strip(), '')
            self.assertEqual(ex.exception.code, 0)
            # commands before quit
            clear_stream(cout)
            with self.assertRaises(SystemExit) as ex:
                cons.onecmd('ls')
                cons.onecmd('quit')
            self.assertEqual(cout.getvalue(), '*** Unknown syntax: ls\n')
            self.assertEqual(ex.exception.code, 0)
            # commands after quit
            clear_stream(cout)
            with self.assertRaises(SystemExit) as ex:
                cons.onecmd('quit')
                cons.onecmd('ls')
            self.assertEqual(cout.getvalue().strip(), '')
            self.assertEqual(cons.lastcmd, 'quit')
            self.assertEqual(ex.exception.code, 0)

    def test_do_show(self):
        """Tests the do_show function of the HBNBCommand class.
        """
        with patch('sys.stdout', new=StringIO()) as cout:
            cons = HBNBCommand()
            reset_store(storage)
            # no arguments
            cons.onecmd('show')
            self.assertEqual(cout.getvalue(), "** class name missing **\n")
            # unknown class
            clear_stream(cout)
            cons.onecmd('show root')
            self.assertEqual(cout.getvalue(), "** class doesn't exist **\n")
            # unknown class with valid instance id
            clear_stream(cout)
            cons.onecmd('create User')
            mdl_id = cout.getvalue().strip()
            clear_stream(cout)
            cons.onecmd('show voot {}'.format(mdl_id))
            self.assertEqual(cout.getvalue(), "** class doesn't exist **\n")
            self.assertIn('User.{}'.format(mdl_id), storage.all())
            # known class with no instance id
            clear_stream(cout)
            cons.onecmd('show User')
            self.assertEqual(cout.getvalue(), "** instance id missing **\n")
            self.assertIn('User.{}'.format(mdl_id), storage.all())
            # known class with unknown instance id
            clear_stream(cout)
            cons.onecmd('show User 444')
            self.assertEqual(cout.getvalue(), "** no instance found **\n")
            self.assertIn('User.{}'.format(mdl_id), storage.all())
            # known class with valid instance id
            clear_stream(cout)
            self.assertIn('User.{}'.format(mdl_id), storage.all())
            cons.onecmd('show User {}'.format(mdl_id))
            self.assertIn('[User] ({})'.format(mdl_id), cout.getvalue())
            self.assertIn('User.{}'.format(mdl_id), storage.all())

    def test_do_update(self):
        """Tests the do_update function of the HBNBCommand class.
        """
        with patch('sys.stdout', new=StringIO()) as cout:
            cons = HBNBCommand()
            reset_store(storage)
            # no arguments
            cons.onecmd('update')
            self.assertEqual(cout.getvalue(), "** class name missing **\n")
            # unknown class
            clear_stream(cout)
            cons.onecmd('update voot')
            self.assertEqual(cout.getvalue(), "** class doesn't exist **\n")
            # unknown class with valid instance id
            clear_stream(cout)
            cons.onecmd('create User')
            mdl_id = cout.getvalue().strip()
            clear_stream(cout)
            cons.onecmd('update voot {}'.format(mdl_id))
            self.assertEqual(cout.getvalue(), "** class doesn't exist **\n")
            self.assertIn('User.{}'.format(mdl_id), storage.all())
            # known class with no instance id
            clear_stream(cout)
            cons.onecmd('update User')
            self.assertEqual(cout.getvalue(), "** instance id missing **\n")
            self.assertIn('User.{}'.format(mdl_id), storage.all())
            # known class with unknown instance id
            clear_stream(cout)
            cons.onecmd('update User 444')
            self.assertEqual(cout.getvalue(), "** no instance found **\n")
            self.assertIn('User.{}'.format(mdl_id), storage.all())
            # known class with unknown instance id and valid attribute
            clear_stream(cout)
            cons.onecmd('update User 444 age')
            self.assertEqual(cout.getvalue(), "** no instance found **\n")
            self.assertIn('User.{}'.format(mdl_id), storage.all())
            # known class, unknown instance id, valid attribute name and value
            clear_stream(cout)
            cons.onecmd('update User 444 age 34')
            self.assertEqual(cout.getvalue(), "** no instance found **\n")
            self.assertIn('User.{}'.format(mdl_id), storage.all())
            # known class, known instance id, no attribute name, no value
            clear_stream(cout)
            cons.onecmd('update User {}'.format(mdl_id))
            self.assertEqual(cout.getvalue(), "** attribute name missing **\n")
            self.assertIn('User.{}'.format(mdl_id), storage.all())
            # known class, known instance id, valid attribute name, no value
            clear_stream(cout)
            cons.onecmd('update User {} age'.format(mdl_id))
            self.assertEqual(cout.getvalue(), "** value missing **\n")
            self.assertIn('User.{}'.format(mdl_id), storage.all())
            # known class, known instance id, valid attribute name, and value
            clear_stream(cout)
            cons.onecmd('update User {} age 34'.format(mdl_id))
            self.assertEqual(cout.getvalue().strip(), "")
            self.assertIn('User.{}'.format(mdl_id), storage.all())
            clear_stream(cout)
            cons.onecmd('show User {}'.format(mdl_id))
            self.assertIn("'age': '34'".format(mdl_id), cout.getvalue())
            self.assertIn('[User] ({})'.format(mdl_id), cout.getvalue())

    def test_cls_all(self):
        """Tests the all class action of the HBNBCommand class.
        """
        with patch('sys.stdout', new=StringIO()) as cout:
            cons = HBNBCommand()
            reset_store(storage)
            self.assertEqual(len(storage.all()), 0)
            # no objects
            cmd_line = cons.precmd('User.all()')
            cons.onecmd(cmd_line)
            self.assertEqual(cout.getvalue(), "[]\n")
            # creating objects and printing them
            clear_stream(cout)
            cons.onecmd('create User')
            mdl_id = cout.getvalue().strip()
            clear_stream(cout)
            cons.onecmd('create User')
            mdl_id1 = cout.getvalue().strip()
            clear_stream(cout)
            cmd_line = cons.precmd('User.all()')
            cons.onecmd(cmd_line)
            self.assertIn('[User] ({})'.format(mdl_id), cout.getvalue())
            self.assertIn('[User] ({})'.format(mdl_id1), cout.getvalue())
            self.assertIn('User.{}'.format(mdl_id), storage.all().keys())
            self.assertIn('User.{}'.format(mdl_id1), storage.all().keys())

    def test_cls_count(self):
        """Tests the count class action of the HBNBCommand class.
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

    def test_cls_destroy(self):
        """Tests the destroy class action of the HBNBCommand class.
        """
        with patch('sys.stdout', new=StringIO()) as cout:
            cons = HBNBCommand()
            reset_store(storage)
            self.assertEqual(len(storage.all()), 0)
            # no id argument
            cmd_line = cons.precmd('User.destroy()')
            cons.onecmd(cmd_line)
            self.assertEqual(cout.getvalue(), "** instance id missing **\n")
            # invalid id argument
            clear_stream(cout)
            cmd_line = cons.precmd('User.destroy("fd34-3e5a")')
            cons.onecmd(cmd_line)
            self.assertEqual(cout.getvalue(), "** no instance found **\n")
            # creating objects and destroying them
            clear_stream(cout)
            cons.onecmd('create User')
            mdl_id = cout.getvalue().strip()
            clear_stream(cout)
            self.assertIn('User.{}'.format(mdl_id), storage.all().keys())
            cmd_line = cons.precmd('User.destroy("{}")'.format(mdl_id))
            cons.onecmd(cmd_line)
            self.assertNotIn('User.{}'.format(mdl_id), storage.all().keys())

    def test_cls_show(self):
        """Tests the show class action of the HBNBCommand class.
        """
        with patch('sys.stdout', new=StringIO()) as cout:
            cons = HBNBCommand()
            reset_store(storage)
            self.assertEqual(len(storage.all()), 0)
            # no id argument
            cmd_line = cons.precmd('User.show()')
            cons.onecmd(cmd_line)
            self.assertEqual(cout.getvalue(), "** instance id missing **\n")
            # invalid id argument
            clear_stream(cout)
            cmd_line = cons.precmd('User.show(34)')
            cons.onecmd(cmd_line)
            self.assertEqual(cout.getvalue(), "** no instance found **\n")
            # creating objects and showing them
            clear_stream(cout)
            cons.onecmd('create User')
            mdl_id = cout.getvalue().strip()
            clear_stream(cout)
            cmd_line = cons.precmd('User.show("{}")'.format(mdl_id))
            cons.onecmd(cmd_line)
            self.assertIn('[User] ({})'.format(mdl_id), cout.getvalue())
            self.assertIn('User.{}'.format(mdl_id), storage.all().keys())

    def test_cls_update(self):
        """Tests the update class action of the HBNBCommand class.
        """
        with patch('sys.stdout', new=StringIO()) as cout:
            cons = HBNBCommand()
            reset_store(storage)
            # create a sample object
            cons.onecmd('create User')
            mdl_id = cout.getvalue().strip()
            # class with no instance id
            clear_stream(cout)
            cmd_line = cons.precmd('User.update()')
            cons.onecmd(cmd_line)
            self.assertEqual(cout.getvalue(), "** instance id missing **\n")
            self.assertIn('User.{}'.format(mdl_id), storage.all().keys())
            # known class with unknown instance id
            clear_stream(cout)
            cmd_line = cons.precmd('User.update("444")')
            cons.onecmd(cmd_line)
            self.assertEqual(cout.getvalue(), "** no instance found **\n")
            self.assertIn('User.{}'.format(mdl_id), storage.all())
            # known class and instance id, no attribute name
            clear_stream(cout)
            cmd_line = cons.precmd('User.update("{}")'.format(mdl_id))
            cons.onecmd(cmd_line)
            self.assertEqual(cout.getvalue(), "** attribute name missing **\n")
            self.assertIn('User.{}'.format(mdl_id), storage.all())
            # known class, unknown instance id, valid attribute name
            clear_stream(cout)
            cmd_line = cons.precmd('User.update("344", "age")')
            cons.onecmd(cmd_line)
            self.assertEqual(cout.getvalue(), "** no instance found **\n")
            self.assertIn('User.{}'.format(mdl_id), storage.all())
            # known class, unknown instance id, valid attribute name and value
            clear_stream(cout)
            cmd_line = cons.precmd('User.update("344", "age", 27)')
            cons.onecmd(cmd_line)
            self.assertEqual(cout.getvalue(), "** no instance found **\n")
            self.assertIn('User.{}'.format(mdl_id), storage.all())
            # known class, known instance id, valid attribute name, no value
            clear_stream(cout)
            cmd_line = cons.precmd(
                'User.update("{}", "first_name")'.format(mdl_id)
            )
            cons.onecmd(cmd_line)
            self.assertEqual(cout.getvalue(), "** value missing **\n")
            self.assertIn('User.{}'.format(mdl_id), storage.all())
            # known class, known instance id, valid attribute name, and value
            clear_stream(cout)
            cmd_line = cons.precmd(
                'User.update("{}", "age", 27)'.format(mdl_id)
            )
            cons.onecmd(cmd_line)
            self.assertEqual(cout.getvalue().strip(), "")
            self.assertIn('User.{}'.format(mdl_id), storage.all())
            clear_stream(cout)
            cmd_line = cons.precmd('User.show("{}")'.format(mdl_id))
            cons.onecmd(cmd_line)
            self.assertIn("'age': '27'".format(mdl_id), cout.getvalue())
            self.assertIn('[User] ({})'.format(mdl_id), cout.getvalue())
            # known class, known instance id, dictionary representation
            clear_stream(cout)
            cmd_line = cons.precmd(
                'User.update("{}"'.format(mdl_id) +
                ", {'bio': 'A kind soul'})"
            )
            cons.onecmd(cmd_line)
            self.assertEqual(cout.getvalue().strip(), "")
            self.assertIn('User.{}'.format(mdl_id), storage.all())
            clear_stream(cout)
            cmd_line = cons.precmd('User.show("{}")'.format(mdl_id))
            cons.onecmd(cmd_line)
            self.assertIn(
                "'bio': 'A kind soul'".format(mdl_id),
                cout.getvalue()
            )
            self.assertIn('[User] ({})'.format(mdl_id), cout.getvalue())
