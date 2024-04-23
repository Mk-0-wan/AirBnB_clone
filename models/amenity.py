#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from sqlalchemy import String, Column
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """Class for amenities"""
    __tablename__ = 'amenities'

    name = Column(
        'name',
        String(128),
        nullable=False
    )
