#!/usr/bin/python3
""" Place Module for HBNB project """
import models
# from os import getenv why does it behave so? when i use getenv??
import os
# what is the table for??
from sqlalchemy import String, Integer, Float, Column, Table, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
# check if this is correct import < from /models/__init__.py

# Ask GPT what's happening
another_table = Base.metadata
place_amenity = Table(
    "place_amenity",
    another_table,
    Column(
        'place_di',
        String(60),
        ForeignKey('places.id'),
        primary_key=True,
        nullable=False
    ),
    Column(
        'amenity_id',
        String(60),
        ForeignKey('amenities.id'),
        primary_key=True,
        nullable=False
    )
)

class Place(BaseModel, Base):
    """ A place to stay """

    # do something
    __tablename__ = "places"

    city_id = Column(
        "city_id",
        String(60),
        ForeignKey("cities.id"),
        nullable=False
    )

    user_id = Column(
        "user_id",
        String(60),
        ForeignKey("users.id"),
        nullable=False
    )

    name = Column(
        "name",
        String(128),
        nullable=False
    )

    description = Column(
        "description",
        String(1024),
        nullable=False
    )

    number_rooms = Column(
        "number_rooms",
        Integer,
        nullable=False,
        default=0
    )

    max_guest = Column(
        "max_guest",
        Integer,
        nullable=False,
        default=0
    )

    price_by_night = Column(
        "price_by_night",
        Integer,
        nullable=False,
        default=0
    )

    latitude = Column(
        "latitude",
        Float,
        nullable=True,
    )

    longitude = Column(
        "longitude",
        Float,
        nullable=True,
    )

    amenity_ids = []

    review = relationship(
        "Review",
        backref="place",
        cascade="all, delete-orphan"
    )

    amenities = relationship(
        "Amenity",
        secondary=place_amenity,
        backref="place_amenities",
        viewonly=False
    )
    amenity_ids = []
    # additional attributes for the places class need to ba accessible even
    # through FileStorage
    @property
    def reivew(self):
        """Getter function to retrive all the reviews related to the
        current place
        """
        review_list = [
            reviews
            for reviews in models.storage.all(models.Review).values()
            if reviews.place_id == self.id
        ]
        return review_list

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def amenities(self):
            """Getter function to retrive all the amenities related to the
            current place
            """
            amenity_list = [
                amenities
                for amenities in models.storage.all(models.Amenity).value()
                if amenities.place_id == self.id
            ]
            return amenity_list

        @amenities.setter
        def amenities(self, amenityObject):
            """Setter function for the amenities_id list"""
            if isinstance(amenityObject, Amenity):
                self.amenity_ids.append(amenityObject.id)

