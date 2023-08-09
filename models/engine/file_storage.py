#!/usr/bin/python3
"""This is a Module for FileStorage class"""
import datetime
import json

class FileStorage:
    """Class for story=ing and retrieving data"""
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """Sets in __objects with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj
    
    def save(self):
        """Serialize __objects to the JSON file in path __file_path"""
        to_hold_dict = FileStorage.__objects
        obj_dict = {obj: to_hold_dict[obj].to_dict() for obj in to_hold_dict.keys()}    
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)
    
    def reload(self):
        """Deserialize JSON file in path __file_path to __objects if it exists"""
        try:
            with open(FileStorage.__file_path) as file:
                obj_dict = json.load(file)
                for item in obj_dict.values():
                    cls_name = item["__class__"]
                    del item["__class__"]
                    self.new(eval(cls_name)(**item))
        except FileNotFoundError:
            return
    