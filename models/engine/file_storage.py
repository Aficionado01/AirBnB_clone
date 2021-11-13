#!/usr/bin/python3
"""A module containing the file storage engine.
"""
import os
from importlib import import_module
from json import JSONDecoder, JSONEncoder


class FileStorage:
    """Represents the file storage for all data sets.
    """
    __file_path = 'file.json'
    __objects = dict()

    def __init__(self):
        """Initializes a FileStorage instance.
        """
        self.model_classes = {
            'BaseModel': import_module('models.base_model').BaseModel,
            'User': import_module('models.user').User,
            'State': import_module('models.state').State,
            'City': import_module('models.city').City,
            'Amenity': import_module('models.amenity').Amenity,
            'Place': import_module('models.place').Place,
            'Review': import_module('models.review').Review
        }

    def all(self):
        """Returns all the stored objects.

        Returns:
            dict: The stored objects.
        """
        return self.__objects

    def new(self, obj):
        """Stores a new object.

        Args:
            obj (BaseModel): The object to store.
        """
        obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[obj_key] = obj

    def save(self):
        """Serializes the objects to a JSON file.
        """
        with open(self.__file_path, mode='w') as file:
            json_objs = {}
            for key, value in self.__objects.items():
                json_objs[key] = value.to_dict()
            file.write(JSONEncoder().encode(json_objs))

    def reload(self):
        """Deserializes the JSON file to objects if it exists.
        """
        if os.path.isfile(self.__file_path):
            file_lines = []
            with open(self.__file_path, mode='r') as file:
                file_lines = file.readlines()
            file_txt = ''.join(file_lines) if len(file_lines) > 0 else '{}'
            json_objs = JSONDecoder().decode(file_txt)
            base_model_objs = dict()
            classes = self.model_classes
            for key, value in json_objs.items():
                cls_name = value['__class__']
                if cls_name in classes.keys():
                    base_model_objs[key] = classes[cls_name](**value)
            self.__objects = base_model_objs
