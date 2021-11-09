#!/usr/bin/python3
"""A module containing the model for amenity data sets.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity data set.
    """
    name = ''
