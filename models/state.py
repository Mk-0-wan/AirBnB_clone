#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
import models

class State(BaseModel, Base):
    """ State class updated with the db storage option"""
    __tablename__ = "states"

    name = Column(
        "name",
        String(128),
        nullable=False
    )

    cities = relationship(
        "City",
        backref="state",
        cascade="all, delete, delete-orphan"
    )

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def getCities(self):
            """getting all the cities associated with the same state.id"""
            city_associated_to_state_list = [
                cities
                for cities in models.storage.all("City").values()
                if cities.id == self.id
            ]
            return city_associate_to_state_list
