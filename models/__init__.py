#!/usr/bin/python3
"""This module instantiates an object of class FileStorage
Initialize the following packages when loaded up
"""

import os
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


if os.getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    CLASSES = {"User": User, "City": City, "State": State, "Place": Place,
            "Review": Review, "Amenity": Amenity, "BaseModel": BaseModel}
else:
    storage = FileStorage()

storage.reload()
