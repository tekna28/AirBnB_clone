#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Represents the HBNBCommand class that defines the command interpreter."""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program (Ctrl-D)."""
        print("")
        return True

    def emptyline(self):
        """Method that handles the emptylines + ENTER."""
        pass

    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
