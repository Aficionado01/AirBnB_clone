#!/usr/bin/python3
"""A module for managing the AirBnB clone's command interpreter.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Represents the command interpreter for the AirBnB clone.
    """
    def __init__(self) -> None:
        """Initializes the AirBnB clone command interpreter.
        """
        super().__init__()
        self.prompt = '(hbnb) '

    def do_EOF(self, args: str):
        """Exits this application.
        Usage: EOF
        """
        exit(0)

    def do_quit(self, args: str):
        """Exits this application.
        Usage: quit
        """
        exit(0)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
