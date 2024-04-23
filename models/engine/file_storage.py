#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if (not cls):
            return FileStorage.__objects
        else:
            res = {}
            for key_object, value_object in FileStorage.__objects.items():
                if (type(value_object) == cls):
                    # adding the key value pair in the new dict
                    res[key_object] = value_object
            return res

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def delete(self, obj=None):
        """To delete an object inside the list of objects
        Arg:
            obj (classObject): an instance of a class e.g State object, Place
            object, Amenity Object and so on.
        Return:
            FileStorage.__object (dict) : a dictionary of key value pairs
            where the key is the {[ClassName](UUID) : {Actual Class Obejct}}
        """
        if (not obj):
            return  None
        else:
            # reverse order of the dict where the key is the value
            # and the value is the key, retrive the key from the reverse dict
            # then delete the value you wanted from the list with the key
            rev = {val: key for key, val in FileStorage.__objects.items()}
            if obj in rev:
                key_to_delete = rev[obj]
                del FileStorage.__objects[key_to_delete]
            return FileStorage.__objects

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
