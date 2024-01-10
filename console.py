#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter
"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    A classe that creat a CLI
    """
    prompt = '(hbnb): '

    def emptyline(self):
        """A method that garanties if an empty line + ENTER
         shouldn’t execute anything
         """
        pass

    def do_EOF(self, line):
        """Quit command to exit the program
        """
        return True

    do_quit = do_EOF

    def do_create(self, arg):
        """A method that creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.

        Ex: $ create BaseModel
        """
        if arg == "":
            print("** class name missing **")
        else:
            class_dict = {"BaseModel": BaseModel, "User": User,
                          "State": State, "City": City, "Amenity": Amenity,
                          "Place": Place, "Review": Review
                          }
            if arg in class_dict:
                obj = class_dict.get(arg, "")()
                print(obj.id)
                models.storage.new(obj)
                models.storage.save()
            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        """A method that prints the string representation of an instance based
        on the class name and id

        Ex: $ show BaseModel 1234-1234-1234.
        """
        lst = [arg for arg in line.split()]
        lenght = len(lst)
        if lenght == 2:
            key = lst[0] + "." + lst[1]
            dictionary_var = models.storage.all()
            if key in dictionary_var:
                print(dictionary_var[key])
            else:
                print("** no instance found **")
        elif lenght == 0:
            print("** class name missing **")
        elif lenght == 1:
            class_dict = {"BaseModel": BaseModel, "User": User,
                          "State": State, "City": City, "Amenity": Amenity,
                          "Place": Place, "Review": Review
                          }
            if lst[0] in class_dict:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, line):
        """A method that deletes an instance based on the class name and id
        (save the change into the JSON file).

        Ex: $ destroy BaseModel 1234-1234-1234.
        """
        lst = [arg for arg in line.split()]
        lenght = len(lst)
        if lenght == 2:
            key = lst[0] + "." + lst[1]
            dictionary_var = models.storage.all()
            if key in dictionary_var:
                del dictionary_var[key]
                models.storage.save()
            else:
                print("** no instance found **")
        elif lenght == 0:
            print("** class name missing **")
        elif lenght == 1:
            class_dict = {"BaseModel": BaseModel, "User": User,
                          "State": State, "City": City, "Amenity": Amenity,
                          "Place": Place, "Review": Review
                          }
            if lst[0] in class_dict:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """A method that prints all string representation of all instances
        based or not on the class name.

        Ex: $ all BaseModel or $ all.
        """
        class_exist = 0
        lst_strings = []
        dictionary_var = models.storage.all()
        if arg != "":
            for ke in dictionary_var.keys():
                if arg in ke:
                    lst_strings.append(str(dictionary_var[ke]))
                    class_exist = 1
            if not class_exist:
                print("** class doesn't exist **")
        else:
            for ke in dictionary_var.keys():
                lst_strings.append(str(dictionary_var[ke]))
        print(lst_strings)

    def do_update(self, line):
        lst = [arg for arg in line.split()]  # we need to impliment a better
        # parsing process to handle the casses where there is "string with
        # space inside a double qoute.

        lenght = len(lst)
        if lenght == 0:
            print("** class name missing **")
        elif lenght == 1:
            class_dict = {"BaseModel": BaseModel, "User": User,
                          "State": State, "City": City, "Amenity": Amenity,
                          "Place": Place, "Review": Review
                          }
            if lst[0] in class_dict:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        elif lenght >= 2:
            cls_id = lst[0] + "." + lst[1]
            dictionary_var = models.storage.all()
            if cls_id in dictionary_var:  # the class.id exist
                if lenght == 2:
                    print("** attribute name missing **")
                elif lenght == 3:
                    print("** value missing **")
                else:
                    setattr(dictionary_var[cls_id], lst[2], lst[3])
                    models.storage.save()
            else:  # the class.id does not exist
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
