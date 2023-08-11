#!/usr/bin/python3
"""The Console module"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from shlex import split
import shlex
class HBNBCommand(cmd.Cmd):
    """The class HBNBCommand"""
    prompt = "(hbnb) "
    classes = {
                  "BaseModel": BaseModel,
                  "User": User,
                  "State": State,
                  "City": City,
                  "Amenity": Amenity,
                  "Place": Place,
                  "Review": Review,
              }
    def strip_args(self, line):
        """stripper() is used to extract arguments inside parentheses"""
        #shlex module is used to handle whitespaces and splitting of arguments
        newstring = line[line.find("(")+1:line.rfind(")")]
        newstring = shlex.shlex(newstring, posix=True)
        newstring.whitespace += ',' # use commas as seperators for tokenization
        newstring.whitespace_split = True
        return list(newstring)
    # whitespace and whitespace_split are attributes
    def dict_strip(self, line):
        """extract dictionary from the input string,
        substring enclosed in curly braces"""
        newstring = line[line.find("(")+1:line.rfind(")")]
        try:
            newdict = newstring[newstring.find("{")+1:newstring.rfind("}")]
            return eval("{" + newdict + "}")
        except:
            return None
# default is used to handle custom functions
    def default(self, line):
        """defaults"""
        subArgs = self.strip_args(line)
        strings = list(shlex.shlex(line, posix=True))
        if strings[0] not in HBNBCommand.classes:
            print("*** Unknown syntax: {}".format(line))
            return
        if strings[2] == "all":
            self.do_all(strings[0])
        elif strings[2] == "count":
            count = 0
            for obj in storage.all().values():
                if strings[0] == type(obj).__name__:
                    count += 1
            print(count)
            return
        elif strings[2] == "show":
            key = strings[0] + " " + subArgs[0]
            self.do_show(key)
        elif strings[2] == "destroy":
            key = strings[0] + " " + subArgs[0]
            self.do_destroy(key)
        elif strings[2] == "update":
            newdict = self.dict_strip(line)
            if type(newdict) is dict:
                for key, val in newdict.items():
                    keyVal = strings[0] + " " + subArgs[0]
                    self.do_update(keyVal + ' "{}" "{}"'.format(key, val))
            else:
                key = strings[0]
                for arg in subArgs:
                    key = key + " " + '"{}"'.format(arg)
                self.do_update(key)
        else:
            print("*** Unknown syntax: {}".format(line))
            return
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Captures Control+D by the User"""
        print()
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
          # all: Prints all string representation
    def do_all(self, line):
        """Prints all instances based on the class name or all instances if no class name is provided."""
    
        if not line:
            all_instances = [str(obj) for obj in storage.all().values()]
            print(all_instances)
            return
    
        class_name = line.split()[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
    
        class_instances = [str(obj) for obj in storage.all().values() if type(obj).__name__ == class_name]
        print(class_instances)
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