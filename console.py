#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""
import cmd
import models
import shlex
import re
import json
from unittest.mock import patch
from io import StringIO
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

    prompt = '(hbnb) '

    class_dict = {"BaseModel": BaseModel, "User": User,
                  "State": State, "City": City, "Amenity": Amenity,
                  "Place": Place, "Review": Review
                  }

    # method_set = {"all", "destroy", "show", "update"}a
    # pt = re.compile(r'\w+(\.)(\w+)(\()(?:.*)(\))')
    # rst = pt.match(st)
    # for i in rst.groups():

    # for meth in method_set:
    # if meth + "("

    def default(self, line):
        """Called on an input line when the command prefix is not recognized.
        """
        ok = 0

        if "count" in line:
            if "." in line:
                lst = line.split(".")
                if "(" in line and ")" in line and "count" in lst[1]:
                    sp_line = line.split(".")[0]
                    print(sum([sp_line in i for i in models.storage.all()]))
                    ok = 1
        elif "{" not in line and ":" not in line:
            if "(" in line and ")" in line:
                try:
                    part_1 = r'(\w+)\.(\w+)\((?:(?:\")?([\w -]*)(?:\")?'
                    part_2 = r'(?:, \"([\w -]*)\"(?:(?:,)? '
                    p3 = r'(?:(?:[\"\']*)?([\d\w.@ -]*)(?:[\"\']*)?).*)?)?)?\)'
                    pt = re.compile(part_1 + part_2 + p3)
                    rst = pt.match(line)
                    arg_lst = []
                    # populate the attribute list, replace None values
                    # with a empty string.
                    for i in rst.groups():
                        if i is not None:
                            arg_lst.append(i)
                        else:
                            arg_lst.append("")
                    cls_nm, method_name, idd, attr_nm, attr_val = arg_lst
                    # check if the idd is space string only and replace it
                    # with default value to net be striped later.
                    if len(idd) and not len(idd.strip()):
                        idd = "default-id"
                    if attr_val == "":
                        r_txt = "{} {} {}"
                        ln_m = r_txt.format(cls_nm, idd, attr_nm, attr_val)
                    else:
                        r_txt = "{} {} {} \"{}\""
                        ln_m = r_txt.format(cls_nm, idd, attr_nm, attr_val)
                    method_dict = {"all": self.do_all,
                                   "destroy": self.do_destroy,
                                   "show": self.do_show,
                                   "update": self.do_update,
                                   }
                    ln_m = ln_m.strip()
                    if method_name in method_dict:
                        # added a space and . to let the do_all method
                        # that the call is from the default method
                        # so the printing should be different task #7 vs #11.
                        if "all" == method_name:
                            method_dict[method_name](ln_m + " .")
                        else:
                            method_dict[method_name](ln_m)
                    ok = 1
                except AttributeError:
                    print("", end="")

        else:
            if "(" in line and ")" in line and "update" in line:
                try:
                    txt_1 = r'(\w+)\.(\w+)\((?:\"([\w-]+)\"'
                    txt_2 = r'(?:, (\{(?:.*)?\})?))?\)'
                    pt = re.compile(txt_1 + txt_2)
                    rst = pt.match(line)
                    arg_lst = []
                    ok = 1
                    for i in rst.groups():
                        if i is not None:
                            arg_lst.append(i)
                        else:
                            arg_lst.append("")
                    cls_nm, method_name, idd, d_str = arg_lst
                    if d_str:
                        dic = json.loads(d_str.replace("'", '"'))
                        if cls_nm in self.class_dict:
                            if len(dic) == 0:
                                print("** attribute name missing **")
                            else:
                                key_val = cls_nm + "." + idd
                                # heck if the class.id does exist
                                if key_val in models.storage.all():
                                    obj = models.storage.all().get(key_val)
                                    for i, j in dic.items():
                                        if len(j) == 0:
                                            print("** value missing **")
                                        else:
                                            setattr(obj, i, j)
                                            models.storage.save()
                                else:  # the class.id does not exist
                                    print("** no instance found **")
                        else:
                            print("** class doesn't exist **")
                except AttributeError:
                    print("", end="")
        if not ok:
            print("*** Unknown syntax:", line)

    def emptyline(self):
        """A method that garanties if an empty line + ENTER
         shouldn’t execute anything
         """
        pass

    def do_EOF(self, line):
        """Quit command to exit the program"""
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
            if arg in self.class_dict:
                obj = self.class_dict.get(arg, "")()
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
            if lst[0] in self.class_dict:
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
            if lst[0] in self.class_dict:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """A method that prints all string representation of all instances
        based or not on the class name.

        Ex: $ all BaseModel or $ all.
        """

        updated_call = 0
        if "." in arg:
            arg = arg.split()[0]
            updated_call = 1
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
        if lst_strings:
            if updated_call:
                print("[" + " ".join(lst_strings) + "]")
            else:
                print(lst_strings)

    def do_update(self, line):
        """A methode that updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).

        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """

        lst = shlex.split(line)

        lenght = len(lst)
        if lenght == 0:
            print("** class name missing **")
        elif lenght == 1:
            if lst[0] in self.class_dict:
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
                    int_fl = lst[3]
                    try:
                        int_fl = int(lst[3])
                    except ValueError:
                        try:
                            int_fl = float(lst[3])
                        except ValueError:
                            int_fl = lst[3]
                    setattr(dictionary_var[cls_id], lst[2], int_fl)
                    models.storage.save()
            else:  # the class.id does not exist
                print("** no instance found **")


if __name__ == '__main__':
    my_cmd = HBNBCommand()
    my_cmd.cmdloop()
