#!/usr/bin/python3
"""A module for managing the AirBnB clone's command interpreter.
"""
import cmd
import re
import shlex
import sys

from models import storage


class HBNBCommand(cmd.Cmd):
    """Represents the command interpreter for the AirBnB clone.
    """
    prompt = '(hbnb) ' if sys.stdin.isatty() else ''

    def preloop(self):
        """Runs some actions before the console's loop begins.
        """
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """Runs some actions before a line of command is executed.

        Args:
            line (str): The line of command to be transformed.
        Returns:
            str: The next line of command to execute.
        """
        patterns = (
            r'(?P<class>[a-zA-Z]+)',
            r'(?P<command>[a-zA-Z]+)',
            r'(?P<args_txt>.*)',
        )
        cls_fxn_fmt = r'{}\s*\.\s*{}\s*\({}\)'.format(
            patterns[0], patterns[1], patterns[2]
        )
        cls_fxn_match = re.fullmatch(cls_fxn_fmt, line)
        if cls_fxn_match is not None:
            class_name = cls_fxn_match.group('class')
            command_name = cls_fxn_match.group('command')
            args_txt = cls_fxn_match.group('args_txt').strip()
            args = None
            cmd_line_parts = []
            try:
                if len(args_txt) == 0:
                    args = tuple()
                else:
                    e = '' if args_txt.endswith(',') else ','
                    args = eval('({}{})'.format(args_txt, e))
                cmd_line_parts.append(command_name)
                cmd_line_parts.append(class_name)
                for arg in args:
                    cmd_line_parts.append('"{}"'.format(arg))
                return ' '.join(cmd_line_parts)
            except Exception:
                return line
        else:
            return line

    def postcmd(self, stop, line):
        """Runs some actions after a line of command is executed.

        Args:
            stop (bool): The continuation condition.
            line (str): The line of command that was executed.

        Returns:
            bool: The continuation condition.
        """
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def emptyline(self):
        """Executes some actions when the command line is empty.

        Returns:
            bool: Always False.
        """
        return False

    def do_EOF(self, line):
        """Exits the console.
        Usage: EOF
        """
        exit(0)

    def do_all(self, line):
        """Prints all instances of a class or all classes.
        Usage: all [<class name>]
        """
        args = shlex.split(line)
        class_name = args[0] if len(args) >= 1 else ''
        if (class_name in storage.model_classes.keys()) or (class_name == ''):
            all_class_objs = []
            for obj in storage.all().values():
                if class_name == '':
                    all_class_objs.append(str(obj))
                elif type(obj) is storage.model_classes[class_name]:
                    all_class_objs.append(str(obj))
            print(all_class_objs)
        else:
            print("** class doesn't exist **")

    def do_count(self, line):
        """Prints the number of instances of a class.
        Usage: count <class name>
        """
        args = shlex.split(line)
        class_name = args[0] if len(args) >= 1 else None
        if class_name is None:
            print("** class name missing **")
            return
        if class_name in storage.model_classes.keys():
            n = 0
            for obj in storage.all().values():
                if type(obj) is storage.model_classes[class_name]:
                    n += 1
            print(n)
        else:
            print("** class doesn't exist **")

    def do_create(self, line):
        """Creates a new instance of a class.
        Usage: create <class name>
        """
        args = shlex.split(line)
        class_name = args[0] if len(args) >= 1 else None
        if class_name is None:
            print("** class name missing **")
            return
        if class_name not in storage.model_classes.keys():
            print("** class doesn't exist **")
            return
        new_obj = storage.model_classes[class_name]()
        new_obj.save()
        print(new_obj.id)

    def do_destroy(self, line):
        """Removes an instance of a class with a given id.
        Usage: destroy <class name> <id>
        """
        args = shlex.split(line)
        class_name = args[0] if len(args) >= 1 else None
        obj_id = args[1] if len(args) >= 2 else None
        obj_store_id = None
        if class_name is None:
            print("** class name missing **")
            return
        if class_name not in storage.model_classes.keys():
            print("** class doesn't exist **")
            return
        if obj_id is None:
            print("** instance id missing **")
            return
        for id, obj in storage.all().items():
            if type(obj) is storage.model_classes[class_name]:
                if obj.id == obj_id:
                    obj_store_id = id
                    break
        if obj_store_id is None:
            print("** no instance found **")
        else:
            storage.all().pop(obj_store_id)
            storage.save()

    def do_quit(self, line):
        """Exits the console.
        Usage: quit
        """
        exit(0)

    def do_show(self, line):
        """Prints an instance of a class with a given id.
        Usage: show <class name> <id>
        """
        args = shlex.split(line)
        class_name = args[0] if len(args) >= 1 else None
        obj_id = args[1] if len(args) >= 2 else None
        if class_name is None:
            print("** class name missing **")
            return
        if class_name not in storage.model_classes.keys():
            print("** class doesn't exist **")
            return
        if obj_id is None:
            print("** instance id missing **")
            return
        for obj in storage.all().values():
            if type(obj) is storage.model_classes[class_name]:
                if obj.id == obj_id:
                    print(obj)
                    return
        print("** no instance found **")

    def do_update(self, line):
        """Updates an instance of a class with a given id.
        Usage: update <class name> <id> <attribute name> <attribute value>
               update <class name> <id> <dictionary representation>
        """
        args = shlex.split(line)
        ignored_attrs = ('id', 'created_at', 'updated_at', '__class__')
        class_name = args[0] if len(args) >= 1 else None
        obj_id = args[1] if len(args) >= 2 else None
        attr_name = args[2] if len(args) >= 3 else None
        attr_value = args[3] if len(args) >= 4 else None
        obj = None
        if class_name is None:
            print("** class name missing **")
            return
        if class_name not in storage.model_classes.keys():
            print("** class doesn't exist **")
            return
        if obj_id is None:
            print("** instance id missing **")
            return
        for store_obj in storage.all().values():
            if type(store_obj) is storage.model_classes[class_name]:
                if store_obj.id == obj_id:
                    obj = store_obj
                    break
        if obj is None:
            print("** no instance found **")
            return
        try:
            dict_src = eval(attr_name)
            if type(dict_src) is dict:
                for key, value in dict_src.items():
                    if key not in ignored_attrs:
                        attr_type = type(getattr(obj.__class__, key, ''))
                        setattr(obj, key, attr_type(value))
                obj.save()
            else:
                raise TypeError()
        except Exception:
            if attr_name is None:
                print("** attribute name missing **")
                return
            if attr_value is None:
                print("** value missing **")
                return
            if attr_name not in ignored_attrs:
                attr_type = type(getattr(obj.__class__, attr_name, ''))
                setattr(obj, attr_name, attr_type(attr_value))
                obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
