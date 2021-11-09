#!/usr/bin/python3
"""Modules for working with data sets.
"""
import models.engine.file_storage as file_storage
# from models.engine.file_storage import FileStorage

# classes = {
#     'BaseModel': import_module('models.base_model').BaseModel,
#     'User': import_module('models.user').User,
#     'State': import_module('models.state').State,
#     'City': import_module('models.city').City,
#     'Amenity': import_module('models.amenity').Amenity,
#     'Place': import_module('models.place').Place,
#     'Review': import_module('models.review').Review,
# }
# storage = FileStorage()
storage = file_storage.FileStorage()
storage.reload()
