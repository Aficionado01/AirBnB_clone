#!/usr/bin/python3
"""A module containing the model for review data sets.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review data set.
    """
    place_id: str = ''
    user_id: str = ''
    text: str = ''
