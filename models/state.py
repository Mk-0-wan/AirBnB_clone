#!/usr/bin/python3
"""Simple state class"""
from models.base_model import BaseModel


class State(BaseModel):
    """State Class
    Args:
        name (string): class attribute containing the state name
    """
    name = ""
