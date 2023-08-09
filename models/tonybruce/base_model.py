import uuid
from datetime import datetime

class BaseModel:
    """Represents the BaseModel class"""
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
    def __str__(self):
        """Return the string representation of the BaseModel instance"""
        # str format: __str__: should print: [<class name>] (<self.id>) <self.__dict__>
        name = self.__class__.__name__# retrieve class name and store in var name
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)
    def save(self):
        """Updates update_at with the current datetime and save"""
        # update_at attribute is used to mark changes to the instance
        self.updated_at = datetime.now()
    def to_dict(self):
        """Returns a dictionary representation of the instance"""
        base_dict = self.__dict__.copy()# create a copy of the instance dictionary
        base_dict["__class__"] = self.__class__.__name__ # add it class name
        base_dict["created_at"] = self.created_at.isoformat() 
        base_dict["updated_at"] = self.updated_at.isoformat()
        # add the created_at and updated_at attribute to the dictionary
        return base_dict
