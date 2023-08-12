#!/usr/bin/python3
"""A Python script that describes the base model"""

import uuid
import models
from datetime import datetime


class BaseModel:
    """Basemodel class that serves as parent class for subsequent classes"""
    def __init__(self, *args, **kwargs):
        """Basemodel initialization"""
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, date_format)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """The string representation of the BaseModel class"""
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id,  self.__dict__)

    def save(self):
        """The "updated_at" is updated with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns the dictionary containing all key/values in instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        return new_dict
