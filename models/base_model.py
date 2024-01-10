#!/usr/bin/python3
"""The Origin of it all the Base Class"""
from datetime import datetime
import uuid
import models


class BaseModel():
    """The first design of the base model"""
    def __init__(self, *args, **kwargs):
        """Initializes an instance with some auto generated instance attributes

        Args:
            id (int): unique user identification helps to keep each instance
                to have a unique id from the rest.
            created_at (datetime): a python datetime object which will always
                be generated each time an instance is created.
            updated_at (datetime): same as created_at only with a slight
                difference updated_at will be updated again
        """

        if kwargs != {}:
            for _key, value in list(kwargs.items()):
                if _key in ["created_at", "updated_at"]:
                    setattr(self, _key, datetime.fromisoformat(value))
                elif _key.startswith("__"):
                    pass
                else:
                    setattr(self, _key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()  # exist in task 3 and not in N4
            models.storage.new(self)

    def save(self):
        """Updates the value of the updated_at attribute"""
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """Return a string representation of the object itself"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """returns a dict representation of all the attributes in it"""
        new_dict = {
                key: value.isoformat()
                if key in ["created_at", "updated_at"] else value
                for key, value in self.__dict__.items()
                }
        new_dict.update({"__class__": type(self).__name__})
        return new_dict
