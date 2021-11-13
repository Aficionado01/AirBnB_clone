#!/usr/bin/python3
"""A module for managing the AirBnB clone's command interpreter.
"""
import cmd
import re
import sys

from models import storage


class HBNBCommand(cmd.Cmd):
    """Represents the command interpreter for the AirBnB clone.
    """

    def __init__(self):
        """Initializes the AirBnB clone command interpreter.
        """
        super().__init__()
        if (not self.stdin.closed) and (self.stdin.isatty()):
            self.prompt = '(hbnb) '
        else:
            self.prompt = '(hbnb) \n'

    @staticmethod
    def split_args(line):
        """Splits a line of arguments.

        Args:
            line (str): The line of arguments separated by spaces.

        Returns:
            list: A list of arguments.
        """
        args_list = []
        txt = line.strip()
        args_match = re.findall(r'(?:"[^"]*"|\S+)\s*', txt)
        if args_match is not None:
            for match in map(lambda x: x.strip(), args_match):
                if match.startswith('"') and match.endswith('"'):
                    args_list.append(match.strip('"'))
                else:
                    args_list.append(match)
        return args_list

    def precmd(self, line):
        """Runs some actions before a line of command is executed.

        Args:
            line (str): The line of command to be executed.
        Returns:
            str: The next line of command to execute.
        """
        patterns = (
            r'(?P<class>[a-zA-Z]+)',
            r'(?P<action>[a-zA-Z]+)',
            r'(?P<args_txt>.*)',
        )
        cls_fxn_fmt = r'{}\s*\.\s*{}\s*\({}\)'.format(
            patterns[0], patterns[1], patterns[2]
        )
        cls_fxn_match = re.fullmatch(cls_fxn_fmt, line)
        if cls_fxn_match is not None:
            class_name = cls_fxn_match.group('class')
            action_name = cls_fxn_match.group('action')
            fxn_name = 'cls_{}'.format(action_name)
            fxn = getattr(self, fxn_name, None)
            args_txt = cls_fxn_match.group('args_txt').strip()
            args = None
            if class_name not in storage.model_classes.keys():
                print("** class doesn't exist **")
                return ''
            if fxn_name not in dir(self):
                # super().onecmd(line)
                return line
            if not isinstance(fxn, type(self.precmd)):
                # super().onecmd(line)
                return line
            try:
                if len(args_txt) == 0:
                    args = tuple()
                else:
                    end_c = '' if args_txt.endswith(',') else ','
                    args = eval('({}{})'.format(args_txt, end_c))
                fxn(class_name, *args)
                return ''
            except Exception:
                # super().onecmd(line)
                return line
        else:
            # super().onecmd(line)
            return line

    def do_EOF(self, line):
        """Exits this application.
        Usage: EOF
        """
        exit(0)

    def do_quit(self, line):
        """Exits this application.
        Usage: quit
        """
        exit(0)

    def emptyline(self):
        """Executes some actions when the command line is empty.

        Returns:
            bool: Always False.
        """
        return False

    def do_create(self, line):
        """Creates a new instance of BaseModel, commits the changes,
        and prints the id.
        Usage: create <class name>
        """
        args = HBNBCommand.split_args(line)
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

    def do_show(self, line):
        """Prints the string representation of an instance based
        on the class name and id
        Usage: show <class name> <id>
        """
        args = HBNBCommand.split_args(line)
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

    def do_destroy(self, line):
        """Deletes an instance based on the class name and
        id and commits the changes.
        Usage: destroy <class name> <id>
        """
        args = HBNBCommand.split_args(line)
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

    def do_all(self, line):
        """Prints the string representation of all types of the
        given class name or any if the class name is omitted.
        Usage: all [<class_name>]
        """
        args = HBNBCommand.split_args(line)
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

    def do_update(self, line):
        """Updates an instance based on the class name and id by
        adding or updating an attribute and commits the changes.
        Usage: update <class name> <id> <attribute_name> <attribute_value>
        """
        args = HBNBCommand.split_args(line)
        ignored_attrs = ('id', 'created_at', 'updated_at')
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
        if attr_name is None:
            print("** attribute name missing **")
            return
        if attr_value is None:
            print("** value missing **")
            return
        if attr_name not in ignored_attrs:
            val = type(getattr(obj, attr_name, ''))(attr_value)
            setattr(obj, attr_name, val)
            obj.save()

    def cls_all(self, class_name, *args):
        """Retrieves all types of a class.

        Args:
            class_name (str): The name of the class.
            args (tuple): The class action's arguments.
        """
        if class_name is None:
            print("** class name missing **")
            return
        if class_name in storage.model_classes.keys():
            all_class_objs = []
            for obj in storage.all().values():
                if type(obj) is storage.model_classes[class_name]:
                    all_class_objs.append(str(obj))
            print('[{}]'.format(', '.join(all_class_objs)))
        else:
            print("** class doesn't exist **")

    def cls_count(self, class_name, *args):
        """Retrieves the number of instances of a class.

        Args:
            class_name (str): The name of the class.
            args (tuple): The class action's arguments.
        """

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

    def cls_show(self, class_name, *args):
        """Retrieves an instances of a class based on its id.

        Args:
            class_name (str): The name of the class.
            args (tuple): The class action's arguments.
        """

        obj_id = args[0] if len(args) >= 1 else None
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

    def cls_destroy(self, class_name, *args):
        """Destroys an instances of a class based on its id.

        Args:
            class_name (str): The name of the class.
            args (tuple): The class action's arguments.
        """

        obj_id = args[0] if len(args) >= 1 else None
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

    def cls_update(self, class_name, *args):
        """Updates and instances of a class based on its id with or
        without a dictionary.

        Args:
            class_name (str): The name of the class.
            args (tuple): The class action's arguments.
        """
        ignored_attrs = ('id', 'created_at', 'updated_at', '__class__')
        obj_id = args[0] if len(args) >= 1 else None
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
        if (len(args) >= 2) and (type(args[1]) is dict):
            dict_src = args[1]
            for key, value in dict_src.items():
                if key not in ignored_attrs:
                    setattr(obj, key, value)
            obj.save()
            return
        attr_name = args[1] if len(args) >= 2 else None
        attr_value = args[2] if len(args) >= 3 else None
        if attr_name is None:
            print("** attribute name missing **")
            return
        if attr_value is None:
            print("** value missing **")
            return
        if attr_name not in ignored_attrs:
            setattr(obj, attr_name, attr_value)
            obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
