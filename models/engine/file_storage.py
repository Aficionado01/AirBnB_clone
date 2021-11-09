#!/usr/bin/python3
"""A module containing the file storage engine.
"""
import os
from json import JSONDecoder, JSONEncoder
from importlib import import_module


class FileStorage:
    """Represents the file storage for all data sets.
    """
    __file_path: str = 'file.json'
    __objects: dict = {}
    __model_classes = {
        'BaseModel': import_module('models.base_model').BaseModel,
        'User': import_module('models.user').User,
    }

    def all(self) -> dict:
        """Returns all the stored objects.

        Returns:
            dict: The stored objects.
        """
        return FileStorage.__objects

    def new(self, obj) -> None:
        """Stores a new object.

        Args:
            obj (BaseModel): The object to store.
        """
        obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[obj_key] = obj

    def save(self):
        """Serializes the objects to a JSON file.
        """
        with open(FileStorage.__file_path, mode='w') as file:
            json_objs = {}
            for key, value in FileStorage.__objects.items():
                json_objs[key] = value.to_dict()
            file.write(JSONEncoder().encode(json_objs))

    def reload(self):
        """Deserializes the JSON file to objects.
        """
        if os.path.isfile(FileStorage.__file_path):
            file_lines = []
            with open(FileStorage.__file_path, mode='r') as file:
                file_lines = file.readlines()
            json_objs = JSONDecoder().decode(''.join(file_lines))
            base_model_objs = {}
            classes = FileStorage.__model_classes
            for key, value in json_objs.items():
                cls_name = value['__class__']
                if cls_name in classes.keys():
                    base_model_objs[key] = classes[cls_name](**value)
            FileStorage.__objects = base_model_objs
