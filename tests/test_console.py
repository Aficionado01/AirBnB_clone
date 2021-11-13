#!/usr/bin/python3
"""A unit test module for the console (command interpreter).
"""
from datetime import datetime
import os
import unittest
from io import StringIO
from unittest.mock import patch

from console import HBNBCommand, storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from tests import remove_files, write_text_file


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
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('create')
            self.assertEqual(istdout.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('create 78')
            self.assertEqual(istdout.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('create 78 User')
            self.assertEqual(istdout.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('create BaseModel')
            self.assertTrue(os.path.isfile('file.json'))
            self.assertTrue(os.stat('file.json').st_size > 20)
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('create City 25')
            self.assertTrue(os.path.isfile('file.json'))
            self.assertTrue(os.stat('file.json').st_size > 20)
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('create "Place"')
            self.assertRegex(
                istdout.getvalue(),
                r'[0-9a-zA-Z]+(?:-[0-9a-zA-Z]+)*\n'
            )
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('create BaseModel')
            self.assertRegex(
                istdout.getvalue(),
                r'[0-9a-zA-Z]+(?:-[0-9a-zA-Z]+)*\n'
            )
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('create User')
            self.assertRegex(
                istdout.getvalue(),
                r'[0-9a-zA-Z]+(?:-[0-9a-zA-Z]+)*\n'
            )
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('create State')
            self.assertRegex(
                istdout.getvalue(),
                r'[0-9a-zA-Z]+(?:-[0-9a-zA-Z]+)*\n'
            )
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('create City')
            self.assertRegex(
                istdout.getvalue(),
                r'[0-9a-zA-Z]+(?:-[0-9a-zA-Z]+)*\n'
            )
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('create Amenity')
            self.assertRegex(
                istdout.getvalue(),
                r'[0-9a-zA-Z]+(?:-[0-9a-zA-Z]+)*\n'
            )
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('create Place')
            self.assertRegex(
                istdout.getvalue(),
                r'[0-9a-zA-Z]+(?:-[0-9a-zA-Z]+)*\n'
            )
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('create Review')
            self.assertRegex(
                istdout.getvalue(),
                r'[0-9a-zA-Z]+(?:-[0-9a-zA-Z]+)*\n'
            )

    def test_do_show(self):
        """Tests the do_show function of the HBNBCommand class.
        """
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('show')
            self.assertEqual(istdout.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('show 78')
            self.assertEqual(istdout.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('show 78 User')
            self.assertEqual(istdout.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('show BaseModel')
            self.assertEqual(istdout.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('show BaseModel ytq')
            self.assertEqual(istdout.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = User()
            mdl.save()
            HBNBCommand().onecmd('show User {}'.format(mdl.id))
            self.assertRegex(
                istdout.getvalue(),
                r'\[User\] \({}\) {}\n'.format(mdl.id, r'\{.+\}')
            )
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = User()
            mdl.save()
            HBNBCommand().onecmd('show BaseModel {}'.format(mdl.id))
            self.assertRegex(
                istdout.getvalue(),
                r'\[User\] \({}\) {}\n'.format(mdl.id, r'\{.+\}')
            )
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = User()
            mdl1 = User()
            mdl.save()
            mdl1.save()
            HBNBCommand().onecmd('show User {} {}'.format(mdl.id, mdl1.id))
            self.assertRegex(
                istdout.getvalue(),
                r'\[User\] \({}\) {}\n'.format(mdl.id, r'\{.+\}')
            )
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = User()
            mdl1 = City()
            mdl.save()
            mdl1.save()
            HBNBCommand().onecmd(
                'show User {} City {}'.format(mdl.id, mdl1.id)
            )
            self.assertRegex(
                istdout.getvalue(),
                r'\[User\] \({}\) {}\n'.format(mdl.id, r'\{.+\}')
            )
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = User()
            mdl1 = User()
            mdl.save()
            mdl1.save()
            HBNBCommand().onecmd(
                'show User {} User {}'.format(mdl.id, mdl1.id)
            )
            self.assertRegex(
                istdout.getvalue(),
                r'\[User\] \({}\) {}\n'.format(mdl.id, r'\{.+\}')
            )
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = User()
            mdl.save()
            HBNBCommand().onecmd('show User %$ {}'.format(mdl.id))
            self.assertEqual(istdout.getvalue(), '** no instance found **\n')

    def test_do_destroy(self):
        """Tests the do_destroy function of the HBNBCommand class.
        """
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('destroy')
            self.assertEqual(istdout.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('destroy 78')
            self.assertEqual(istdout.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('destroy 78 User')
            self.assertEqual(istdout.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('destroy City')
            self.assertEqual(istdout.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('destroy Review ytq')
            self.assertEqual(istdout.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = User()
            mdl.save()
            self.assertIn(mdl, storage.all().values())
            HBNBCommand().onecmd('destroy User {}'.format(mdl.id))
            self.assertEqual(istdout.getvalue(), '')
            self.assertNotIn(mdl, storage.all().values())
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = User()
            mdl.save()
            self.assertIn(mdl, storage.all().values())
            HBNBCommand().onecmd('destroy BaseModel {}'.format(mdl.id))
            self.assertEqual(istdout.getvalue(), '')
            self.assertNotIn(mdl, storage.all().values())
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = User()
            mdl1 = User()
            mdl.save()
            mdl1.save()
            self.assertIn(mdl, storage.all().values())
            self.assertIn(mdl1, storage.all().values())
            HBNBCommand().onecmd('destroy User {} {}'.format(mdl.id, mdl1.id))
            self.assertEqual(istdout.getvalue(), '')
            self.assertNotIn(mdl, storage.all().values())
            self.assertIn(mdl1, storage.all().values())
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = User()
            mdl1 = City()
            mdl.save()
            mdl1.save()
            self.assertIn(mdl, storage.all().values())
            self.assertIn(mdl1, storage.all().values())
            HBNBCommand().onecmd(
                'destroy User {} City {}'.format(mdl.id, mdl1.id)
            )
            self.assertEqual(istdout.getvalue(), '')
            self.assertNotIn(mdl, storage.all().values())
            self.assertIn(mdl1, storage.all().values())
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = User()
            mdl1 = User()
            mdl.save()
            mdl1.save()
            self.assertIn(mdl, storage.all().values())
            self.assertIn(mdl1, storage.all().values())
            HBNBCommand().onecmd(
                'destroy User {} User {}'.format(mdl.id, mdl1.id)
            )
            self.assertEqual(istdout.getvalue(), '')
            self.assertNotIn(mdl, storage.all().values())
            self.assertIn(mdl1, storage.all().values())
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = User()
            mdl.save()
            self.assertIn(mdl, storage.all().values())
            HBNBCommand().onecmd('destroy User %$ {}'.format(mdl.id))
            self.assertEqual(istdout.getvalue(), '** no instance found **\n')
            self.assertIn(mdl, storage.all().values())

    def test_do_all(self):
        """Tests the do_all function of the HBNBCommand class.
        """
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('all 78')
            self.assertEqual(istdout.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('all 78 User')
            self.assertEqual(istdout.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('all BaseModel')
            self.assertEqual(istdout.getvalue(), "[]\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('all User')
            self.assertEqual(istdout.getvalue(), "[]\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('all State')
            self.assertEqual(istdout.getvalue(), "[]\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('all City')
            self.assertEqual(istdout.getvalue(), "[]\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('all Amenity')
            self.assertEqual(istdout.getvalue(), "[]\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('all Place')
            self.assertEqual(istdout.getvalue(), "[]\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('all Review')
            self.assertEqual(istdout.getvalue(), "[]\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('all Review 25')
            self.assertEqual(istdout.getvalue(), "[]\n")
        # testing non-empty output
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = BaseModel()
            storage.save()
            HBNBCommand().onecmd('all BaseModel')
            self.assertRegex(
                istdout.getvalue(),
                r'\["\[BaseModel\] \({}\) {}"\]\n'.format(mdl.id, r'\{.+\}')
            )
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = BaseModel()
            storage.save()
            HBNBCommand().onecmd('all')
            self.assertRegex(
                istdout.getvalue(),
                r'\["\[BaseModel\] \({}\) {}"\]\n'.format(mdl.id, r'\{.+\}')
            )
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = User()
            storage.save()
            HBNBCommand().onecmd('all User')
            self.assertRegex(
                istdout.getvalue(),
                r'\["\[User\] \({}\) {}"\]\n'.format(mdl.id, r'\{.+\}')
            )
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = User()
            storage.save()
            HBNBCommand().onecmd('all')
            self.assertRegex(
                istdout.getvalue(),
                r'\["\[User\] \({}\) {}"\]\n'.format(mdl.id, r'\{.+\}')
            )
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = State()
            storage.save()
            HBNBCommand().onecmd('all State')
            self.assertRegex(
                istdout.getvalue(),
                r'\["\[State\] \({}\) {}"\]\n'.format(mdl.id, r'\{.+\}')
            )
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = State()
            storage.save()
            HBNBCommand().onecmd('all')
            self.assertRegex(
                istdout.getvalue(),
                r'\["\[State\] \({}\) {}"\]\n'.format(mdl.id, r'\{.+\}')
            )
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = City()
            storage.save()
            HBNBCommand().onecmd('all City')
            self.assertRegex(
                istdout.getvalue(),
                r'\["\[City\] \({}\) {}"\]\n'.format(mdl.id, r'\{.+\}')
            )
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = City()
            storage.save()
            HBNBCommand().onecmd('all')
            self.assertRegex(
                istdout.getvalue(),
                r'\["\[City\] \({}\) {}"\]\n'.format(mdl.id, r'\{.+\}')
            )
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = Amenity()
            storage.save()
            HBNBCommand().onecmd('all Amenity')
            self.assertRegex(
                istdout.getvalue(),
                r'\["\[Amenity\] \({}\) {}"\]\n'.format(mdl.id, r'\{.+\}')
            )
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = Amenity()
            storage.save()
            HBNBCommand().onecmd('all')
            self.assertRegex(
                istdout.getvalue(),
                r'\["\[Amenity\] \({}\) {}"\]\n'.format(mdl.id, r'\{.+\}')
            )
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = Place()
            storage.save()
            HBNBCommand().onecmd('all Place')
            self.assertRegex(
                istdout.getvalue(),
                r'\["\[Place\] \({}\) {}"\]\n'.format(mdl.id, r'\{.+\}')
            )
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = Place()
            storage.save()
            HBNBCommand().onecmd('all')
            self.assertRegex(
                istdout.getvalue(),
                r'\["\[Place\] \({}\) {}"\]\n'.format(mdl.id, r'\{.+\}')
            )
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = Review()
            storage.save()
            HBNBCommand().onecmd('all Review')
            self.assertRegex(
                istdout.getvalue(),
                r'\["\[Review\] \({}\) {}"\]\n'.format(mdl.id, r'\{.+\}')
            )
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = Review()
            storage.save()
            HBNBCommand().onecmd('all')
            self.assertRegex(
                istdout.getvalue(),
                r'\["\[Review\] \({}\) {}"\]\n'.format(mdl.id, r'\{.+\}')
            )
        # mixed models
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = User()
            mdl1 = City()
            storage.save()
            HBNBCommand().onecmd('all')
            self.assertRegex(
                istdout.getvalue(),
                r'\["\[User\] \({}\) {}"'.format(mdl.id, r'\{.+\}')
                + r', "\[City\] \({}\) {}"\]\n'.format(mdl1.id, r'\{.+\}')
            )
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = Review()
            storage.save()
            HBNBCommand().onecmd('all Review 23')
            self.assertRegex(
                istdout.getvalue(),
                r'\["\[Review\] \({}\) {}"\]\n'.format(mdl.id, r'\{.+\}')
            )

    def test_do_update(self):
        """Tests the do_update function of the HBNBCommand class.
        """
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('update')
            self.assertEqual(istdout.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('update 78')
            self.assertEqual(istdout.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('update 78 User')
            self.assertEqual(istdout.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('update City')
            self.assertEqual(istdout.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('update Review ytq')
            self.assertEqual(istdout.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('update State gggh name California')
            self.assertEqual(istdout.getvalue(), "** no instance found **\n")
        mdl_s = City()
        mdl_s.save()
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().onecmd('update City {}'.format(mdl_s.id))
            self.assertEqual(
                istdout.getvalue(),
                "** attribute name missing **\n"
            )
        with patch('sys.stdout', new=StringIO()) as istdout:
            self.assertEqual(mdl_s.name, '')
            HBNBCommand().onecmd('update City {} name'.format(mdl_s.id))
            self.assertEqual(istdout.getvalue(), "** value missing **\n")
            self.assertEqual(mdl_s.name, '')
        with patch('sys.stdout', new=StringIO()) as istdout:
            self.assertEqual(mdl_s.name, '')
            if os.path.isfile('file.json'):
                os.unlink('file.json')
            self.assertFalse(os.path.isfile('file.json'))
            HBNBCommand().onecmd('update City {} name Paris'.format(mdl_s.id))
            self.assertEqual(istdout.getvalue(), "")
            self.assertTrue(os.path.isfile('file.json'))
            self.assertEqual(mdl_s.name, 'Paris')
        # only one attribute can be updated in a single command line
        with patch('sys.stdout', new=StringIO()) as istdout:
            self.assertNotEqual(mdl_s.name, 'Madrid')
            self.assertFalse(hasattr(mdl_s, 'population'))
            HBNBCommand().onecmd(
                'update City {} name Madrid population 345'.format(mdl_s.id)
            )
            self.assertEqual(istdout.getvalue(), "")
            self.assertEqual(mdl_s.name, 'Madrid')
            self.assertFalse(hasattr(mdl_s, 'population'))
        # id, created_at, and updated_at can't be updated
        with patch('sys.stdout', new=StringIO()) as istdout:
            self.assertNotEqual(mdl_s.id, 'c-589')
            HBNBCommand().onecmd(
                'update City {} id c-589'.format(mdl_s.id)
            )
            self.assertEqual(istdout.getvalue(), "")
            self.assertNotEqual(mdl_s.id, 'c-589')
        with patch('sys.stdout', new=StringIO()) as istdout:
            time_s = datetime(2003, 5, 15)
            self.assertNotEqual(mdl_s.created_at, time_s)
            HBNBCommand().onecmd(
                'update City {} created_at "{}"'.format(
                    mdl_s.id, time_s.isoformat()
                    )
            )
            self.assertEqual(istdout.getvalue(), "")
            self.assertNotEqual(mdl_s.created_at, time_s)
        with patch('sys.stdout', new=StringIO()) as istdout:
            time_s = datetime(2003, 5, 15)
            self.assertNotEqual(mdl_s.updated_at, time_s)
            HBNBCommand().onecmd(
                'update City {} updated_at "{}"'.format(
                    mdl_s.id, time_s.isoformat()
                    )
            )
            self.assertEqual(istdout.getvalue(), "")
            self.assertNotEqual(mdl_s.updated_at, time_s)

    def test_class_action(self):
        """Tests the class action syntax of the HBNBCommand class.
        """
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().precmd('foo.a')
            self.assertEqual(istdout.getvalue(), "*** Unknown syntax: foo.a\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().precmd('User.a')
            self.assertEqual(
                istdout.getvalue(),
                "*** Unknown syntax: User.a\n"
            )
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().precmd('User.all')
            self.assertEqual(
                istdout.getvalue(),
                "*** Unknown syntax: User.all\n"
            )
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().precmd('User.all(')
            self.assertEqual(
                istdout.getvalue(),
                "*** Unknown syntax: User.all(\n"
            )
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().precmd('User.all)')
            self.assertEqual(
                istdout.getvalue(),
                "*** Unknown syntax: User.all)\n"
            )
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().precmd('User.all(")')
            self.assertEqual(
                istdout.getvalue(),
                "*** Unknown syntax: User.all(\")\n"
            )
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().precmd('User.all(1 23)')
            self.assertEqual(
                istdout.getvalue(),
                "*** Unknown syntax: User.all(1 23)\n"
            )
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().precmd('User.foo()')
            self.assertEqual(
                istdout.getvalue(),
                "*** Unknown syntax: User.foo()\n"
            )
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().precmd('ghy.foo()')
            self.assertEqual(istdout.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().precmd('.all()')
            self.assertEqual(
                istdout.getvalue(),
                "*** Unknown syntax: .all()\n"
            )
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().precmd('User.()')
            self.assertEqual(
                istdout.getvalue(),
                "*** Unknown syntax: User.()\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().precmd('User()')
            self.assertEqual(
                istdout.getvalue(),
                "*** Unknown syntax: User()\n"
            )
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().precmd('User.show "49faff9a-6318-451f-87b6"')
            self.assertEqual(
                istdout.getvalue(),
                '*** Unknown syntax: User.show "49faff9a-6318-451f-87b6"\n'
            )
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().precmd('foo.all()')
            self.assertEqual(istdout.getvalue(), "** class doesn't exist **\n")

    def test_cls_all(self):
        """Tests the all class action of the HBNBCommand class.
        """
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            self.assertEqual(len(storage.all()), 0)
            HBNBCommand().precmd('User.all()')
            self.assertEqual(istdout.getvalue(), "[]\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            self.assertEqual(len(storage.all()), 0)
            HBNBCommand().precmd('User.all("49faff9a-6318-451f-87b6")')
            self.assertEqual(istdout.getvalue(), "[]\n")
        # creating objects and showing them
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = BaseModel()
            mdl.save()
            HBNBCommand().precmd('BaseModel.all()')
            self.assertRegex(
                istdout.getvalue(),
                r'\[\[BaseModel\] \({}\) {}\]\n'.format(mdl.id, r'\{.+\}')
            )
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = Amenity()
            mdl.save()
            HBNBCommand().precmd('BaseModel.all()')
            self.assertRegex(
                istdout.getvalue(),
                r'\[\[Amenity\] \({}\) {}\]\n'.format(mdl.id, r'\{.+\}')
            )
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = User()
            mdl.save()
            HBNBCommand().precmd('User.all()')
            self.assertRegex(
                istdout.getvalue(),
                r'\[\[User\] \({}\) {}\]\n'.format(mdl.id, r'\{.+\}')
            )
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = State()
            mdl.save()
            HBNBCommand().precmd('State.all()')
            self.assertRegex(
                istdout.getvalue(),
                r'\[\[State\] \({}\) {}\]\n'.format(mdl.id, r'\{.+\}')
            )
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = City()
            mdl.save()
            HBNBCommand().precmd('City.all()')
            self.assertRegex(
                istdout.getvalue(),
                r'\[\[City\] \({}\) {}\]\n'.format(mdl.id, r'\{.+\}')
            )
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = Amenity()
            mdl.save()
            HBNBCommand().precmd('Amenity.all()')
            self.assertRegex(
                istdout.getvalue(),
                r'\[\[Amenity\] \({}\) {}\]\n'.format(mdl.id, r'\{.+\}')
            )
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = Place()
            mdl.save()
            HBNBCommand().precmd('Place.all()')
            self.assertRegex(
                istdout.getvalue(),
                r'\[\[Place\] \({}\) {}\]\n'.format(mdl.id, r'\{.+\}')
            )
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = Review()
            mdl.save()
            HBNBCommand().precmd('Review.all()')
            self.assertRegex(
                istdout.getvalue(),
                r'\[\[Review\] \({}\) {}\]\n'.format(mdl.id, r'\{.+\}')
            )
        # creating multiple objects and showing them
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            a = City()
            b = City()
            a.save()
            b.save()
            HBNBCommand().precmd('City.all()')
            self.assertRegex(
                istdout.getvalue(),
                r'\[\[City\] \(({}|{})\) {}, '.format(a.id, b.id, r'\{.+\}')
                + r'\[City\] \(({}|{})\) {}\]\n'.format(a.id, b.id, r'\{.+\}')
            )

    def test_cls_count(self):
        """Tests the count class action of the HBNBCommand class.
        """
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            self.assertEqual(len(storage.all()), 0)
            HBNBCommand().precmd('User.count("49faff9a-6318-451f-87b6")')
            self.assertEqual(istdout.getvalue(), "0\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            self.assertEqual(len(storage.all()), 0)
            HBNBCommand().precmd('User.count(None)')
            self.assertEqual(istdout.getvalue(), "0\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            self.assertEqual(len(storage.all()), 0)
            HBNBCommand().precmd('User.count()')
            self.assertEqual(istdout.getvalue(), "0\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            self.assertEqual(len(storage.all()), 0)
            HBNBCommand().precmd('BaseModel.count()')
            self.assertEqual(istdout.getvalue(), "0\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            self.assertEqual(len(storage.all()), 0)
            HBNBCommand().precmd('State.count()')
            self.assertEqual(istdout.getvalue(), "0\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            self.assertEqual(len(storage.all()), 0)
            HBNBCommand().precmd('City.count()')
            self.assertEqual(istdout.getvalue(), "0\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            self.assertEqual(len(storage.all()), 0)
            HBNBCommand().precmd('Amenity.count()')
            self.assertEqual(istdout.getvalue(), "0\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            self.assertEqual(len(storage.all()), 0)
            HBNBCommand().precmd('Place.count()')
            self.assertEqual(istdout.getvalue(), "0\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            self.assertEqual(len(storage.all()), 0)
            HBNBCommand().precmd('Review.count()')
            self.assertEqual(istdout.getvalue(), "0\n")
        # creating objects and counting them
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            BaseModel().save()
            Review().save()
            HBNBCommand().precmd('BaseModel.count()')
            self.assertEqual(istdout.getvalue(), '2\n')
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            User().save()
            User().save()
            HBNBCommand().precmd('User.count()')
            self.assertEqual(istdout.getvalue(), '2\n')
        remove_files()
        with patch('sys.stdout', new=StringIO()) as istdout:
            State().save()
            State().save()
            State().save()
            HBNBCommand().precmd('State.count()')
            self.assertEqual(istdout.getvalue(), '3\n')
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            City().save()
            City().save()
            City().save()
            City().save()
            HBNBCommand().precmd('City.count()')
            self.assertEqual(istdout.getvalue(), '4\n')
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            Amenity().save()
            Amenity().save()
            Amenity().save()
            HBNBCommand().precmd('Amenity.count()')
            self.assertEqual(istdout.getvalue(), '3\n')
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            Place().save()
            Place().save()
            HBNBCommand().precmd('Place.count()')
            self.assertEqual(istdout.getvalue(), '2\n')
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            Review().save()
            Review().save()
            Review().save()
            HBNBCommand().precmd('Review.count()')
            self.assertEqual(istdout.getvalue(), '3\n')
        write_text_file('file.json', '{}')
        storage.reload()

    def test_cls_show(self):
        """Tests the show class action of the HBNBCommand class.
        """
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().precmd('User.show()')
            self.assertEqual(istdout.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().precmd('User.show("49faff9a-6318-451f-87b6")')
            self.assertEqual(istdout.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().precmd('User.show(2)')
            self.assertEqual(istdout.getvalue(), "** no instance found **\n")
        # creating objects and showing them
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = BaseModel()
            mdl.save()
            HBNBCommand().precmd('BaseModel.show("{}")'.format(mdl.id))
            self.assertRegex(
                istdout.getvalue(),
                r'\[BaseModel\] \({}\) {}\n'.format(mdl.id, r'\{.+\}')
            )
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = Amenity()
            mdl.save()
            HBNBCommand().precmd('BaseModel.show("{}")'.format(mdl.id))
            self.assertRegex(
                istdout.getvalue(),
                r'\[Amenity\] \({}\) {}\n'.format(mdl.id, r'\{.+\}')
            )
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = User()
            mdl.save()
            HBNBCommand().precmd('User.show("{}")'.format(mdl.id))
            self.assertRegex(
                istdout.getvalue(),
                r'\[User\] \({}\) {}\n'.format(mdl.id, r'\{.+\}')
            )
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = State()
            mdl.save()
            HBNBCommand().precmd('State.show("{}")'.format(mdl.id))
            self.assertRegex(
                istdout.getvalue(),
                r'\[State\] \({}\) {}\n'.format(mdl.id, r'\{.+\}')
            )
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = City()
            mdl.save()
            HBNBCommand().precmd('City.show("{}")'.format(mdl.id))
            self.assertRegex(
                istdout.getvalue(),
                r'\[City\] \({}\) {}\n'.format(mdl.id, r'\{.+\}')
            )
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = Amenity()
            mdl.save()
            HBNBCommand().precmd('Amenity.show("{}")'.format(mdl.id))
            self.assertRegex(
                istdout.getvalue(),
                r'\[Amenity\] \({}\) {}\n'.format(mdl.id, r'\{.+\}')
            )
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = Place()
            mdl.save()
            HBNBCommand().precmd('Place.show("{}")'.format(mdl.id))
            self.assertRegex(
                istdout.getvalue(),
                r'\[Place\] \({}\) {}\n'.format(mdl.id, r'\{.+\}')
            )
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = Review()
            mdl.save()
            HBNBCommand().precmd('Review.show("{}")'.format(mdl.id))
            self.assertRegex(
                istdout.getvalue(),
                r'\[Review\] \({}\) {}\n'.format(mdl.id, r'\{.+\}')
            )
        # creating objects and showing them (with multiple arguments)
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = BaseModel()
            mdl.save()
            HBNBCommand().precmd('BaseModel.show("{}", 34)'.format(mdl.id))
            self.assertRegex(
                istdout.getvalue(),
                r'\[BaseModel\] \({}\) {}\n'.format(mdl.id, r'\{.+\}')
            )
        write_text_file('file.json', '{}')
        storage.reload()

    def test_cls_destroy(self):
        """Tests the destroy class action of the HBNBCommand class.
        """
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().precmd('User.destroy()')
            self.assertEqual(istdout.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().precmd('User.destroy("49faff9a-6318-451f-87b6")')
            self.assertEqual(istdout.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().precmd('User.destroy(2)')
            self.assertEqual(istdout.getvalue(), "** no instance found **\n")
        # creating objects and destroying them
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = State()
            mdl.save()
            self.assertIn('State.{}'.format(mdl.id), storage.all().keys())
            HBNBCommand().precmd('BaseModel.destroy("{}")'.format(mdl.id))
            self.assertEqual(istdout.getvalue(), '')
            self.assertNotIn('State.{}'.format(mdl.id), storage.all().keys())
        # only instances of the respective class can be destroyed
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            mdl = State()
            mdl.save()
            self.assertIn('State.{}'.format(mdl.id), storage.all().keys())
            HBNBCommand().precmd('Amenity.destroy("{}")'.format(mdl.id))
            self.assertEqual(istdout.getvalue(), '** no instance found **\n')
            self.assertIn('State.{}'.format(mdl.id), storage.all().keys())
        # only one item can be destroyed in each line
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            a = State()
            b = State()
            a.save()
            b.save()
            self.assertIn('State.{}'.format(a.id), storage.all().keys())
            self.assertIn('State.{}'.format(b.id), storage.all().keys())
            HBNBCommand().precmd(
                'State.destroy("{}", "{}")'.format(a.id, b.id)
            )
            self.assertEqual(istdout.getvalue(), '')
            self.assertNotIn('State.{}'.format(a.id), storage.all().keys())
            self.assertIn('State.{}'.format(b.id), storage.all().keys())

    def test_cls_update(self):
        """Tests the update class action of the HBNBCommand class.
        """
        write_text_file('file.json', '{}')
        storage.reload()
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().precmd('City.update()')
            self.assertEqual(istdout.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().precmd('Review.update("ytq")')
            self.assertEqual(istdout.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().precmd('State.update("gggh", "name", "California")')
            self.assertEqual(istdout.getvalue(), "** no instance found **\n")
        mdl_s = City()
        mdl_s.save()
        with patch('sys.stdout', new=StringIO()) as istdout:
            HBNBCommand().precmd('City.update("{}")'.format(mdl_s.id))
            self.assertEqual(
                istdout.getvalue(),
                "** attribute name missing **\n"
            )
        with patch('sys.stdout', new=StringIO()) as istdout:
            self.assertEqual(mdl_s.name, '')
            HBNBCommand().precmd('City.update("{}", "name")'.format(mdl_s.id))
            self.assertEqual(istdout.getvalue(), "** value missing **\n")
            self.assertEqual(mdl_s.name, '')
        with patch('sys.stdout', new=StringIO()) as istdout:
            self.assertEqual(mdl_s.name, '')
            if os.path.isfile('file.json'):
                os.unlink('file.json')
            self.assertFalse(os.path.isfile('file.json'))
            HBNBCommand().precmd(
                'City.update("{}", "name", "Paris")'.format(mdl_s.id)
            )
            self.assertEqual(istdout.getvalue(), "")
            self.assertTrue(os.path.isfile('file.json'))
            self.assertEqual(mdl_s.name, 'Paris')
        # only one attribute can be updated in a single command line
        with patch('sys.stdout', new=StringIO()) as istdout:
            self.assertNotEqual(mdl_s.name, 'Madrid')
            self.assertFalse(hasattr(mdl_s, 'nm'))
            self.assertFalse(hasattr(mdl_s, 'population'))
            HBNBCommand().precmd(
                'City.update("{}", "nm", "Madrid", "population", 345)'
                .format(mdl_s.id)
            )
            self.assertEqual(istdout.getvalue(), "")
            self.assertTrue(hasattr(mdl_s, 'nm'))
            self.assertFalse(hasattr(mdl_s, 'population'))
            self.assertEqual(getattr(mdl_s, 'nm'), 'Madrid')
        # id, created_at, and updated_at can't be updated
        with patch('sys.stdout', new=StringIO()) as istdout:
            self.assertNotEqual(mdl_s.id, 'c-589')
            HBNBCommand().precmd(
                'City.update("{}", "id", "c-589")'.format(mdl_s.id)
            )
            self.assertEqual(istdout.getvalue(), "")
            self.assertNotEqual(mdl_s.id, 'c-589')
        with patch('sys.stdout', new=StringIO()) as istdout:
            time_s = datetime(2003, 5, 15)
            self.assertNotEqual(mdl_s.created_at, time_s)
            HBNBCommand().precmd(
                'City.update("{}", "created_at", "{}")'.format(
                    mdl_s.id, time_s.isoformat()
                    )
            )
            self.assertEqual(istdout.getvalue(), "")
            self.assertNotEqual(mdl_s.created_at, time_s)
        with patch('sys.stdout', new=StringIO()) as istdout:
            time_s = datetime(2003, 5, 15)
            self.assertNotEqual(mdl_s.updated_at, time_s)
            HBNBCommand().precmd(
                'City.update("{}", "updated_at", "{}")'.format(
                    mdl_s.id, time_s.isoformat()
                    )
            )
            self.assertEqual(istdout.getvalue(), "")
            self.assertNotEqual(mdl_s.updated_at, time_s)
        # region Using a dictionary representation
        mdl_s = User()
        mdl_s.save()
        with patch('sys.stdout', new=StringIO()) as istdout:
            if os.path.isfile('file.json'):
                os.unlink('file.json')
            self.assertFalse(os.path.isfile('file.json'))
            self.assertFalse(hasattr(mdl_s, 'age'))
            HBNBCommand().precmd(
                'User.update("{}", {{\'age\': 5}}, "Paris")'.format(mdl_s.id)
            )
            self.assertEqual(istdout.getvalue(), "")
            self.assertTrue(os.path.isfile('file.json'))
            self.assertTrue(hasattr(mdl_s, 'age'))
            self.assertEqual(getattr(mdl_s, 'age'), 5)
            self.assertFalse(hasattr(mdl_s, "{'age': 5}"))
        with patch('sys.stdout', new=StringIO()) as istdout:
            self.assertFalse(hasattr(mdl_s, 'j'))
            self.assertFalse(hasattr(mdl_s, 'IQ'))
            HBNBCommand().precmd(
                'User.update("{}", {{\'j\': 3}}, "IQ", "50")'.format(mdl_s.id)
            )
            self.assertEqual(istdout.getvalue(), '')
            self.assertFalse(hasattr(mdl_s, 'IQ'))
            self.assertTrue(hasattr(mdl_s, 'j'))
            self.assertEqual(getattr(mdl_s, 'j'), 3)
        # id, __class__ created_at, and updated_at can't be updated
        with patch('sys.stdout', new=StringIO()) as istdout:
            self.assertEqual(mdl_s.to_dict()['__class__'], 'User')
            HBNBCommand().precmd(
                'User.update("{}", {{\'__class__\': "rt"}})'.format(mdl_s.id)
            )
            self.assertEqual(istdout.getvalue(), '')
            self.assertEqual(mdl_s.to_dict()['__class__'], 'User')
            self.assertNotEqual(mdl_s.to_dict()['__class__'], 'rt')
        with patch('sys.stdout', new=StringIO()) as istdout:
            self.assertNotEqual(mdl_s.id, 'c-589')
            HBNBCommand().precmd(
                'User.update("{}", {{"id": "c-589"}})'.format(mdl_s.id)
            )
            self.assertEqual(istdout.getvalue(), "")
            self.assertNotEqual(mdl_s.id, 'c-589')
        with patch('sys.stdout', new=StringIO()) as istdout:
            time_s = datetime(2003, 5, 15)
            self.assertNotEqual(mdl_s.created_at, time_s)
            HBNBCommand().precmd(
                'User.update("{}", {{"created_at": "{}"}})'.format(
                    mdl_s.id, time_s.isoformat()
                    )
            )
            self.assertEqual(istdout.getvalue(), "")
            self.assertNotEqual(mdl_s.created_at, time_s)
        with patch('sys.stdout', new=StringIO()) as istdout:
            time_s = datetime(2003, 5, 15)
            self.assertNotEqual(mdl_s.updated_at, time_s)
            HBNBCommand().precmd(
                'User.update("{}", {{"updated_at": "{}"}})'.format(
                    mdl_s.id, time_s.isoformat()
                    )
            )
            self.assertEqual(istdout.getvalue(), "")
            self.assertNotEqual(mdl_s.updated_at, time_s)
        # endregion
