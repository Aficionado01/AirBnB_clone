#!/usr/bin/python3
"""Modules for working with data sets.
"""
from models.engine.file_storage import FileStorage
import models.amenity
import models.base_model
import models.city
import models.place
import models.review
import models.state
import models.user


storage = FileStorage()
"""A unique FileStorage instance for all models.
"""
storage.reload()
