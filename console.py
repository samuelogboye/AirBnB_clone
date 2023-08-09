#!/usr/bin/python3
"""The Console module"""
import cmd

class HBNBCommand(cmd.Cmd):
    """The class HBNBCommand"""
    prompt = "(hbnb) "
    
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, line):
        """Captures Control+D by the User"""
        return True
    
    def emptyline(self):
        """An empty line+ENter should not execute anything"""
        pass
    
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()