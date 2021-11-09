#!/usr/bin/python3
"""A module containing the model for place data sets.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents a place data set.
    """
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
