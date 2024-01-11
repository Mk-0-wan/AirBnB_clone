#!/usr/bin/python3
"""Simple state class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity Class
    Args:
        name (string): class attribute containing the Amenity name
    """
    name = ""
