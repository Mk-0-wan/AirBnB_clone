#!/usr/bin/env python3
"""Simple DBStorage implementation"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.city import City
from models.state import State
from models.base_model import BaseModel, Base

class DBStorage:
    """ Database Storage type (aka mysql_database)"""
    __engine = None
    __session = None

    def __init__(self):
        username = os.getenv("HBNB_MYSQL_USER")
        passwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        database = os.getenv("HBNB_MYSQL_DB")
        environ = os.getenv("HBNB_MYSQL_ENV")
        self.__engine = create_engine('mysql+mysqldb'
            '://{}:{}@{}/{}'
            .format(
                username,
                passwd,
                host,
                database
            ),
            pool_pre_ping=True # allows you to have multiple pre instanciated
            # objects from these instance alone (allowing you to have multiple
            # connections)
        )

        if environ == "test":
            # change of environemnt means we need new setting up to do and the
            # above created orm(sort of database should be dropped immedately)
            Base.metadata.drop_all(self.__engine)


    def all(self, cls=None):
        """ Returns all the matching objects from the database
        Args:
            cls(Object) : instance of a class among the CLASSES instances,
            if provided return only the object matching the class instance
        Return:
            return a dict containing a list of all objects matching the cls
        """
        import models

        DB_DICT = {}
        classDict = models.CLASSES

        if (cls):
            if cls in classDict:
                class_obj = self.__session.query(classDict[cls]).all()
                for obj in class_obj:
                    key = obj.__class__.__name__ + '.' + obj.id
                    DB_DICT[key] = obj
            return DB_DICT
        else:
            for _, value in classDict.items():
                try:
                    # trying to grab the objects(AKA attributes)
                    class_obj = self.__session.query(value).all()
                    # print(class_obj)
                except Exception as e:
                    # print(f"******Error:[{e}]*****")
                    continue
                for obj in class_obj:
                    key = obj.__class__.__name__ + '.' + obj.id
                    DB_DICT[key] = obj
            return DB_DICT

    def get(self, cls, id):
        """Retrive one object if exist
        """
        classDict = self.all(cls)
        for k, v in classDict.items():
            obj = cls + '.' + id
            if k == obj:
                return v
        return None

    def new(self, obj):
        """Just add a new object to the current session running"""
        self.__session.add(obj)

    def save(self):
        """Commit all the changes made on the current running session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete the object from the session(imagine it as an open database
        to changes at any moment)"""
        if (obj is not None):
            self.__session.delete(obj)

    def reload(self):
        """The engine creator of the whole session and establishing of both the
        tables and the ORM functionalities"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        )
        Session = scoped_session(session_factory)

        self.__session = Session()
