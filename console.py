#!/usr/bin/python3
"""A module for managing the AirBnB clone's command interpreter.
"""
import enum
import cmd
import re
from importlib import import_module
from models import storage


class ErrorTypes(enum.IntEnum):
    """The types of command errors in this command interpreter.
    """
    Class_Name_Missing = 0
    Class_Missing = 1
    Instance_Id_Missing = 2
    Instance_Missing = 3
    Attribute_Name_Missing = 4
    Attribute_Missing = 5


class HBNBCommand(cmd.Cmd):
    """Represents the command interpreter for the AirBnB clone.
    """
    model_classes = {
        'BaseModel': import_module('models.base_model').BaseModel,
        'User': import_module('models.user').User,
    }
    error_messages: tuple = (
        "** class name missing **",
        "** class doesn't exist **",
        "** instance id missing **",
        "** no instance found **",
        "** attribute name missing **",
        "** value missing **",
    )

    def __init__(self) -> None:
        """Initializes the AirBnB clone command interpreter.
        """
        super().__init__()
        self.prompt = '(hbnb) '

    @staticmethod
    def split_args(line: str):
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
            for match in args_match:
                if match.startswith('"') and match.endswith('"'):
                    args_list.append(match.strip('"'))
                else:
                    args_list.append(match.strip())
        return args_list

    def do_EOF(self, line: str) -> None:
        """Exits this application.
        Usage: EOF
        """
        exit(0)

    def do_quit(self, line: str) -> None:
        """Exits this application.
        Usage: quit
        """
        exit(0)

    def do_create(self, line: str) -> None:
        """Creates a new instance of BaseModel, commits the changes,
        and prints the id.
        Usage: create <class name>
        """
        errors = HBNBCommand.error_messages
        args = HBNBCommand.split_args(line)
        class_name = args[0] if len(args) >= 1 else None
        if class_name is None:
            print(errors[ErrorTypes.Class_Name_Missing])
            return
        if class_name not in HBNBCommand.model_classes.keys():
            print(errors[ErrorTypes.Class_Missing])
            return
        new_obj = HBNBCommand.model_classes[class_name]()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, line: str) -> None:
        """Prints the string representation of an instance based
        on the class name and id
        Usage: show <class name> <id>
        """
        errors = HBNBCommand.error_messages
        args = HBNBCommand.split_args(line)
        class_name = args[0] if len(args) >= 1 else None
        obj_id = args[1] if len(args) >= 2 else None
        if class_name is None:
            print(errors[ErrorTypes.Class_Name_Missing])
            return
        if class_name not in HBNBCommand.model_classes.keys():
            print(errors[ErrorTypes.Class_Missing])
            return
        if obj_id is None:
            print(errors[ErrorTypes.Instance_Id_Missing])
            return
        for obj in storage.all().values():
            if isinstance(obj, HBNBCommand.model_classes[class_name]):
                if obj.id == obj_id:
                    print(obj)
                    return
        print(errors[ErrorTypes.Instance_Missing])

    def do_destroy(self, line: str) -> None:
        """Deletes an instance based on the class name and
        id and commits the changes.
        Usage: destroy <class name> <id>
        """
        errors = HBNBCommand.error_messages
        args = HBNBCommand.split_args(line)
        class_name = args[0] if len(args) >= 1 else None
        obj_id = args[1] if len(args) >= 2 else None
        obj_store_id = None
        if class_name is None:
            print(errors[ErrorTypes.Class_Name_Missing])
            return
        if class_name not in HBNBCommand.model_classes.keys():
            print(errors[ErrorTypes.Class_Missing])
            return
        if obj_id is None:
            print(errors[ErrorTypes.Instance_Id_Missing])
            return
        for id, obj in storage.all().items():
            if isinstance(obj, HBNBCommand.model_classes[class_name]):
                if obj.id == obj_id:
                    obj_store_id = id
                    break
        if obj_store_id is None:
            print(errors[ErrorTypes.Instance_Missing])
        else:
            storage.all().pop(obj_store_id)
            storage.save()

    def do_all(self, line: str) -> None:
        """Prints the string representation of all instances of the given class name.
        Usage: all [<class_name>]
            <class_name> - One of the values in the set {BaseModel, User}.
                Default: BaseModel.
        """
        args = HBNBCommand.split_args(line)
        class_name = args[0] if len(args) >= 1 else 'BaseModel'
        if class_name in HBNBCommand.model_classes.keys():
            all_class_objs = []
            for obj in storage.all().values():
                if isinstance(obj, HBNBCommand.model_classes[class_name]):
                    all_class_objs.append(str(obj))
            print(all_class_objs)
        else:
            print("** class doesn't exist **")

    def do_update(self, line: str) -> None:
        """Updates an instance based on the class name and id by adding or updating
        an attribute and commits the changes.
        Usage: update <class name> <id> <attribute_name> <attribute_value>
        """
        errors = HBNBCommand.error_messages
        args = HBNBCommand.split_args(line)
        ignored_attrs = ('id', 'created_at', 'updated_at')
        class_name = args[0] if len(args) >= 1 else None
        obj_id = args[1] if len(args) >= 2 else None
        attr_name = args[2] if len(args) >= 3 else None
        attr_value = args[3] if len(args) >= 4 else None
        obj = None
        if class_name is None:
            print(errors[ErrorTypes.Class_Name_Missing])
            return
        if class_name not in HBNBCommand.model_classes.keys():
            print(errors[ErrorTypes.Class_Missing])
            return
        if obj_id is None:
            print(errors[ErrorTypes.Instance_Id_Missing])
            return
        for store_obj in storage.all().values():
            if isinstance(store_obj, HBNBCommand.model_classes[class_name]):
                if store_obj.id == obj_id:
                    obj = store_obj
                    break
        if obj is None:
            print(errors[ErrorTypes.Instance_Missing])
            return
        if attr_name is None:
            print(errors[ErrorTypes.Attribute_Name_Missing])
            return
        if attr_value is None:
            print(errors[ErrorTypes.Attribute_Missing])
            return
        if attr_name not in ignored_attrs:
            val = type(getattr(obj, attr_name, ''))(attr_value)
            setattr(obj, attr_name, val)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
