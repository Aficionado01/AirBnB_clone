#!/usr/bin/python3
"""A module containing the model for user data sets.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents the base class for all user data sets.
    """
    email: str = ''
    password: str = ''
    first_name: str = ''
    last_name: str = ''
