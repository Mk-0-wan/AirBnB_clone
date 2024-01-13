#!/usr/bin/python3
"""
This module contains a class called FileStorage
"""
import json
from pathlib import Path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """A file storage class which has methods which will work well
    with the console

    Args:
        __file_path (file): json file to store each instance of an object
        __objects (dictionary): a dict holding all the objs class name, and id
    """
    # to check full path vs relative path
    __file_path = "models/engine/file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Collects the object from another class and then stores its
        to the __object dictionary

        Dict format { <class_name>.<object.id> : <object> }

        Args:
            obj (class Instance): a python object which is an instance of the
            class BaseModel at the moment
        """
        self.__objects.update({f"{type(obj).__name__}.{obj.id}": obj})

    def save(self):
        """
        serializes __objects to the JSON
        stores it to file (path: __file_path)
        all the objects are now further extracted to their unique attributes
        """
        tmp_dict = {}
        for key, value in self.__objects.items():
            tmp_dict[key] = value.to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(tmp_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)
        """
        if Path(self.__file_path).is_file():
            class_dict = {"BaseModel": BaseModel, "User": User,
                          "State": State, "City": City, "Amenity": Amenity,
                          "Place": Place, "Review": Review
                          }
            with open(self.__file_path, "r", encoding="utf-8") as f:
                red = f.read()
                if red != "":
                    dicts = json.loads(red)
                    for k, v in dicts.items():
                        for key in class_dict.keys():
                            if key in k:
                                self.__objects[k] = class_dict[key](**v)
