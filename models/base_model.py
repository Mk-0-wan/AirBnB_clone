#!/usr/bin/python3
"""The Origin of it all the Base Class"""
from datetime import datetime
import uuid


class BaseModel():
    """The first design of the base model"""
    def __init__(self, id=str(uuid.uuid4()), created_at=datetime.now(),
                 updated_at=datetime.now(), *args, **kwargs):
        """Initializes an instance with some auto generated instance attributes

        Args:
            id (int): unique user identification helps to keep each instance
                to have a unique id from the rest.
            created_at (datetime): a python datetime object which will always
                be generated each time an instance is created.
            updated_at (datetime): same as created_at only with a slight
                difference updated_at will be updated again
        """
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        if kwargs is not None:
            for _key, value in list(kwargs.items()):
                if _key in ["created_at", "updated_at"]:
                    kwargs[_key] = datetime.fromisoformat(value)
                elif _key.startswith("__"):
                    del kwargs[_key]

    def save(self):
        """Updates the value of the updated_at attribute"""
        self.updated_at = datetime.now()

    def __str__(self):
        """Return a string representation of the object itself"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """returns a dict representation of all the attributes in it"""
        new_dict = {
                key : value.isoformat()
                if key in ["created_at", "updated_at"] else value
                for key, value in self.__dict__.items()
                }
        new_dict.update({"__class__": type(self).__name__})
        return new_dict

# just for testing
if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
    print("--------")
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

    print("--------")
    print(my_model is my_new_model)
