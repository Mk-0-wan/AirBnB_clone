
#!/usr/bin/python3
"""Simple state class"""
from models.base_model import BaseModel


class City(BaseModel):
    """City Class
    Args:
        state_id (string): class attributes containing the state.id
        name (string): class attribute containing the state name
    """
    name = ""
    state_id = ""
