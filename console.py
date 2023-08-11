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
import re
import json

"""
from shlex import split
import shlex
"""


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
    """
    def strip_args(self, line):
        newstring = line[line.find("(")+1:line.rfind(")")]
        newstring = shlex.shlex(newstring, posix=True)
        newstring.whitespace += ','
        newstring.whitespace_split = True
        return list(newstring)
    # whitespace and whitespace_split are attributes
    """
    def dict_strip(self, line):
        """extract dictionary from the input string,
        substring enclosed in curly braces"""
        newstring = line[line.find("(")+1:line.rfind(")")]
        try:
            newdict = newstring[newstring.find("{")+1:newstring.rfind("}")]
            return eval("{" + newdict + "}")
        except ValueError:
            return None

    def default(self, line):
        """defaults to handle custom functions"""
        """
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
        """
        self._precmd(line)    
    
    def _precmd(self, line):
        """Intercepts commands to test for class.syntax()"""
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line
        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        attr_and_value = ""
        if method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""
            match_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(
                    1) or "") + " " + (match_attr_and_value.group(2) or "")
        command = method + " " + classname + " " + uid + " " + attr_and_value
        self.onecmd(command)
        return command
    
    def update_dict(self, classname, uid, s_dict):
        """Helper method for update() with a dictionary."""
        s = s_dict.replace("'", '"')
        d = json.loads(s)
        if not classname:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[classname]
                for attribute, value in d.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()
    
    def do_count(self, line):
        """Counts the instances of a class.
        """
        words = line.split(' ')
        if not words[0]:
            print("** class name missing **")
        elif words[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            matches = [
                k for k in storage.all() if k.startswith(
                    words[0] + '.')]
            print(len(matches))
    
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

    def do_create(self, class_name):
        # do_create is used to create objects
        """ Creates a new instance of BaseModel"""
        if not class_name:
            print("** class name missing **")
            return
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
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

    def do_all(self, line):
        """Prints all instances based on the class name or
        all instances if no class name is provided."""
    
        if not line:
            all_instances = [str(obj) for obj in storage.all().values()]
            print(all_instances)
            return
    
        class_name = line.split()[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
    
        class_instances = [
            str(obj)
            for obj in storage.all().values()
            if type(obj).__name__ == class_name]
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
    