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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
