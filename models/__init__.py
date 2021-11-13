#!/usr/bin/python3
"""Modules for working with data sets.
"""
from models.engine.file_storage import FileStorage


models = {}
"""The models in this project.
"""
storage = FileStorage()
"""A unique FileStorage instance for all models.
"""


def import_models():
    '''import modules after instantiating a storage instace
    to fix circular imports'''
    global models
    from .base_model import BaseModel
    from .amenity import Amenity
    from .city import City
    from .place import Place
    from .review import Review
    from .state import State
    from .user import User

    models = {c.__name__: c
              for c in [BaseModel, Amenity, City, Place, Review, State, User]}

import_models()
storage.reload()
