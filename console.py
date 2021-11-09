#!/usr/bin/python3
"""A module for managing the AirBnB clone's command interpreter.
"""
import enum
import cmd
import re
from models import storage


class ErrorTypes(enum.IntEnum):
    """The types of command errors in this command interpreter.
    """
    Class_Name_Missing = 0
    Class_Not_Existing = 1
    Instance_Id_Missing = 2
    Instance_Not_Existing = 3
    Attribute_Name_Missing = 4
    Attribute_Value_Missing = 5


class HBNBCommand(cmd.Cmd):
    """Represents the command interpreter for the AirBnB clone.
    """
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

    def precmd(self, line: str) -> str:
        """Runs some actions before a line of command is executed.

        Args:
            line (str): The line of command to be executed.
        Returns:
            str: The next line of command to execute.
        """
        errors = HBNBCommand.error_messages
        patterns = (
            r'(?P<class>[a-zA-Z]+)',
            r'(?P<action>[a-zA-Z]+)',
            r'(?P<args_txt>.*)',
            # r'(?P<int_t>[-+]?\d+)',
            # r'(?P<float_t>[-+]?\d+\.\d+)',
            # r'(?P<string_t>"(?:[^"]|\\")*")',
            # r'(?P<dict_t>\{.*\})',
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
                print(errors[ErrorTypes.Class_Not_Existing])
                return ''
            if fxn_name not in dir(self):
                return super().precmd(line)
            if isinstance(fxn, type(self.precmd)):
                return super().precmd(line)
            try:
                if len(args_txt) == 0:
                    args = tuple()
                else:
                    end_c = '' if args_txt.endswith(',') else ','
                    args = eval('({}{})'.format(args_txt, end_c))
                fxn(class_name, *args)
            except Exception:
                return super().precmd(line)
            return ''
        else:
            return super().precmd(line)

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

    def emptyline(self) -> bool:
        """Executes some actions when the command line is empty.

        Returns:
            bool: Always False.
        """
        return False

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
        if class_name not in storage.model_classes.keys():
            print(errors[ErrorTypes.Class_Not_Existing])
            return
        new_obj = storage.model_classes[class_name]()
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
        if class_name not in storage.model_classes.keys():
            print(errors[ErrorTypes.Class_Not_Existing])
            return
        if obj_id is None:
            print(errors[ErrorTypes.Instance_Id_Missing])
            return
        for obj in storage.all().values():
            if isinstance(obj, storage.model_classes[class_name]):
                if obj.id == obj_id:
                    print(obj)
                    return
        print(errors[ErrorTypes.Instance_Not_Existing])

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
        if class_name not in storage.model_classes.keys():
            print(errors[ErrorTypes.Class_Not_Existing])
            return
        if obj_id is None:
            print(errors[ErrorTypes.Instance_Id_Missing])
            return
        for id, obj in storage.all().items():
            if isinstance(obj, storage.model_classes[class_name]):
                if obj.id == obj_id:
                    obj_store_id = id
                    break
        if obj_store_id is None:
            print(errors[ErrorTypes.Instance_Not_Existing])
        else:
            storage.all().pop(obj_store_id)
            storage.save()

    def do_all(self, line: str) -> None:
        """Prints the string representation of all instances of the
        given class name.
        Usage: all [<class_name>]
            <class_name> - One of the values in the set {BaseModel, User}.
                Default: BaseModel.
        """
        errors = HBNBCommand.error_messages
        args = HBNBCommand.split_args(line)
        class_name = args[0] if len(args) >= 1 else 'BaseModel'
        if class_name in storage.model_classes.keys():
            all_class_objs = []
            for obj in storage.all().values():
                if isinstance(obj, storage.model_classes[class_name]):
                    all_class_objs.append(str(obj))
            print(all_class_objs)
        else:
            print(errors[ErrorTypes.Class_Not_Existing])

    def do_update(self, line: str) -> None:
        """Updates an instance based on the class name and id by
        adding or updating an attribute and commits the changes.
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
        if class_name not in storage.model_classes.keys():
            print(errors[ErrorTypes.Class_Not_Existing])
            return
        if obj_id is None:
            print(errors[ErrorTypes.Instance_Id_Missing])
            return
        for store_obj in storage.all().values():
            if isinstance(store_obj, storage.model_classes[class_name]):
                if store_obj.id == obj_id:
                    obj = store_obj
                    break
        if obj is None:
            print(errors[ErrorTypes.Instance_Not_Existing])
            return
        if attr_name is None:
            print(errors[ErrorTypes.Attribute_Name_Missing])
            return
        if attr_value is None:
            print(errors[ErrorTypes.Attribute_Value_Missing])
            return
        if attr_name not in ignored_attrs:
            val = type(getattr(obj, attr_name, ''))(attr_value)
            setattr(obj, attr_name, val)

    def cls_all(self, class_name: str, *args: tuple):
        """Retrieves all instances of a class.

        Args:
            class_name (str): The name of the class.
            args (tuple): The class action's arguments.
        """
        errors = HBNBCommand.error_messages
        if class_name is None:
            print(errors[ErrorTypes.Class_Name_Missing])
            return
        if class_name in storage.model_classes.keys():
            all_class_objs = []
            for obj in storage.all().values():
                if isinstance(obj, storage.model_classes[class_name]):
                    all_class_objs.append(str(obj))
            print(all_class_objs)
        else:
            print(errors[ErrorTypes.Class_Not_Existing])

    def cls_count(self, class_name: str, *args: tuple) -> None:
        """Retrieves the number of instances of a class.

        Args:
            class_name (str): The name of the class.
            args (tuple): The class action's arguments.
        """
        errors = HBNBCommand.error_messages
        if class_name is None:
            print(errors[ErrorTypes.Class_Name_Missing])
            return
        if class_name in storage.model_classes.keys():
            n = 0
            for obj in storage.all().values():
                if isinstance(obj, storage.model_classes[class_name]):
                    n += 1
            print(n)
        else:
            print(errors[ErrorTypes.Class_Not_Existing])

    def cls_show(self, class_name: str, *args: tuple) -> None:
        """Retrieves an instances of a class based on its id.

        Args:
            class_name (str): The name of the class.
            args (tuple): The class action's arguments.
        """
        errors = HBNBCommand.error_messages
        obj_id = args[0] if len(args) >= 1 else None
        if class_name is None:
            print(errors[ErrorTypes.Class_Name_Missing])
            return
        if class_name not in storage.model_classes.keys():
            print(errors[ErrorTypes.Class_Not_Existing])
            return
        if obj_id is None:
            print(errors[ErrorTypes.Instance_Id_Missing])
            return
        for obj in storage.all().values():
            if isinstance(obj, storage.model_classes[class_name]):
                if obj.id == obj_id:
                    print(obj)
                    return
        print(errors[ErrorTypes.Instance_Not_Existing])

    def cls_destroy(self, class_name: str, *args: tuple) -> None:
        """Destroys an instances of a class based on its id.

        Args:
            class_name (str): The name of the class.
            args (tuple): The class action's arguments.
        """
        errors = HBNBCommand.error_messages
        obj_id = args[0] if len(args) >= 1 else None
        obj_store_id = None
        if class_name is None:
            print(errors[ErrorTypes.Class_Name_Missing])
            return
        if class_name not in storage.model_classes.keys():
            print(errors[ErrorTypes.Class_Not_Existing])
            return
        if obj_id is None:
            print(errors[ErrorTypes.Instance_Id_Missing])
            return
        for id, obj in storage.all().items():
            if isinstance(obj, storage.model_classes[class_name]):
                if obj.id == obj_id:
                    obj_store_id = id
                    break
        if obj_store_id is None:
            print(errors[ErrorTypes.Instance_Not_Existing])
        else:
            storage.all().pop(obj_store_id)
            storage.save()

    def cls_update(self, class_name: str, *args: tuple) -> None:
        """Updates and instances of a class based on its id with or
        without a dictionary.

        Args:
            class_name (str): The name of the class.
            args (tuple): The class action's arguments.
        """
        errors = HBNBCommand.error_messages
        ignored_attrs = ('id', 'created_at', 'updated_at')
        obj_id = args[0] if len(args) >= 1 else None
        obj = None
        if class_name is None:
            print(errors[ErrorTypes.Class_Name_Missing])
            return
        if class_name not in storage.model_classes.keys():
            print(errors[ErrorTypes.Class_Not_Existing])
            return
        if obj_id is None:
            print(errors[ErrorTypes.Instance_Id_Missing])
            return
        for store_obj in storage.all().values():
            if isinstance(store_obj, storage.model_classes[class_name]):
                if store_obj.id == obj_id:
                    obj = store_obj
                    break
        if obj is None:
            print(errors[ErrorTypes.Instance_Not_Existing])
            return
        if (len(args) >= 2) and (type(args[1]) is dict):
            dict_src = args[1]
            for key, value in dict_src.items():
                if key not in ignored_attrs:
                    setattr(obj, key, value)
            return
        attr_name = args[1] if len(args) >= 2 else None
        attr_value = args[2] if len(args) >= 3 else None
        if attr_name is None:
            print(errors[ErrorTypes.Attribute_Name_Missing])
            return
        if attr_value is None:
            print(errors[ErrorTypes.Attribute_Value_Missing])
            return
        if attr_name not in ignored_attrs:
            setattr(obj, attr_name, attr_value)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
