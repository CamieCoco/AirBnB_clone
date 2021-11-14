#!/usr/bin/python3
"""
Contains class BaseModel
"""

from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """The BaseModel class from whichthe other classes will be derived"""

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, val in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        time = "%Y-%m-%dT%H:%M:%S.%f"
        dic = self.__dict__.copy()
        if "created_at" in dic:
            dic["created_at"] = dic["created_at"].strftime(time)
        if "updated_at" in dic:
            dic["updated_at"] = dic["updated_at"].strftime(time)
        dic["__class__"] = self.__class__.__name__
        return dic
