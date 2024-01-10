#!/usr/bin/python3
"""User Class which inherits from the BaseModel Class"""
from models.base_model import BaseModel


class User(BaseModel):
    """User that inherits from BaseModel

    Args:
        email (string): string representation of the user email address
        password (string): string representation of the user password
        first_name (string): Public class attr holding the user name
        last_name (string): Public class attr holding the user last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
