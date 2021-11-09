#!/usr/bin/python3
"""A module containing the model for city data sets.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city data set.
    """
    state_id = ''
    name = ''
