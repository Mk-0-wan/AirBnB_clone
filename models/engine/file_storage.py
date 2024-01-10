#!/usr/bin/python3
"""
This module contains a class called FileStorage
"""
import json
from pathlib import Path
from models.base_model import BaseModel
from models.user import User 


class FileStorage():
    """
    A class that serializes instances to a JSON file and deserializes
    JSON file to instances
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
        A method that sets in __objects the obj with key <obj class name>.id
        """
        self.__objects.update({f"{type(obj).__name__}.{obj.id}": obj})
        # print("#############")
        # for ob in self.__objects.values():
            # print("------: ",ob, "----" )
        # print("#############")
        # print(self.__objects)

    def save(self):
        """
        A method that serializes __objects to the JSON file (path: __file_path)
        """
        tmp_dict = {}
        for k, v in self.__objects.items():
            tmp_dict[k] = v.to_dict()
        objects_json_str = json.dumps(tmp_dict)
        with open(self.__file_path, "w", encoding="utf-8") as f:
            f.write(objects_json_str)

    def reload(self):
        """
        A method that deserializes the JSON file to __objects if the file exist
        """
        if Path(self.__file_path).is_file():
            class_dict = {"BaseModel": BaseModel, "User": User}
            with open(self.__file_path, "r", encoding="utf-8") as f:
                red = f.read()
                dicts = json.loads(red)
                for k, v in dicts.items():
                    for key in class_dict.keys():
                        if key in k:
                            self.__objects[k] = class_dict[key](**v)
