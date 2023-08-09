#!/usr/bin/python3
"""A Python script that describes the base model"""

import uuid
from datetime import datetime


class BaseModel:
    """Basemodel class that serves as parent class for subsequent classes"""
    def __init__(self, *args, **kwargs):
        """Basemodel initialization"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
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
