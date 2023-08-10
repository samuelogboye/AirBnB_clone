#!/usr/bin/python3
"""The Console module"""
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """The class HBNBCommand"""
    prompt = "(hbnb) "
    
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, line):
        """Captures Control+D by the User"""
        print() # to print a newline btw the previous command output and the console prompt
        return True
    
    def emptyline(self):
        """An empty line+ENter should not execute anything"""
        pass
    # create command, takes self(instance) and className as args
    def do_create(self, class_name):
        # do_create is used to create objects
        """ Creates a new instance of BaseModel"""
        if not class_name:
            print("** class name missing **")
            return
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return #in case of error, the return exits the do_create method
        new_obj = eval(class_name)()
        print(new_obj.id)
        new_obj.save()
    # show command, Prints the string representation of an instance based on the class name and id
    def do_show(self, args):
        """string representation of objects"""
        if not args:
            print("** class name missing **")
            return
        str = split(args)
        if str[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(str) == 1:
            print("** instance id missing **")
            return
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
