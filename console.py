#!/usr/bin/python3
"""The Console module"""
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """The class HBNBCommand"""
    prompt = "(hbnb) "
    classes = {"BaseModel",
               "User"}
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
        strings = args.split()
        if strings[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(strings) == 1:
            print("** instance id missing **")
            return
        key_value = strings[0] + '.' + strings[1]
        if key_value not in storage.all().keys():
            print("** no instance found **")
        else:
            print(storage.all()[key_value])
    def do_destroy(self, args):
          """deletes an instance based on the class name and id"""
          if not args:
              print("** class name missing **")
              return
          strings = args.split()
          if strings[0] not in HBNBCommand.classes:
              print("** class doesn't exist **")
              return
          if len(strings) == 1:
              print("** instance id missing **")
              return
          key_value = strings[0] + '.' + strings[1]
          if key_value not in storage.all().keys():
              print("** no instance found **")
              return
          del storage.all()[key_value]
          storage.save()
          # all: Prints all string representation of all instances based
    def do_all(self, args):
        """prints all string representation of all instances based 
            or not on the class name"""
        
        if args != "":
            strings = args.split(' ')
            if strings[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                final_string = [str(obj) for key, obj in storage.all().items()
                                if type(obj).__name__ == strings[0]]
                print(final_string)
        else:
            new_list =  [str(obj) for key, obj in storage.all().items()]
            print(new_list)                      
    
    def do_update(self, args):
        """updates an object"""
        if not args:
            print("** class name missing **")
            return
        strings = args.split()
        for string in strings:
            if string.startswith('"') and string.endswith('"'):
                string = string[1:-1]
        if strings[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(strings) == 1:
            print("** instance id missing **")
            return
        key_value = strings[0] + '.' + strings[1]
        if key_value not in storage.all().keys():
            print("** no instance found **")
            return
        if len(strings) == 2:
            print("** attribute name missing **")
            return
        if len(strings) == 3:
            print("** value missing **")
            return
        try:
            setattr(storage.all()[key_value], strings[2], eval(strings[3]))
        except ValueError:
            setattr(storage.all()[key_value], strings[2], strings[3])
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
