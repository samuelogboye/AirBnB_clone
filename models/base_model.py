#!/usr/bin/python3
"""A Python script that describes the base model"""

import uuid
from datetime import datetime


class BaseModel:
    """Basemodel class that serves as parent class for subsequent classes"""
    def __init__(self, *args, **kwargs):
        """Basemodel initialization"""
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """The string representation of the BaseModel class"""
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id,  self.__dict__)

    def save(self):
        """The "updated_at" is updated with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns the dictionary containing all key/values in instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        return new_dict
