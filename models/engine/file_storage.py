#!/usr/bin/python3
''' module for FileStorage class '''
import json
from os.path import isfile


class FileStorage:
    ''' class for persistent storage '''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        ''' gets all objects '''
        return self.__objects

    def new(self, obj):
        ''' registers a new object '''
        pass

    def save(self):
        ''' saves all objects to a file '''
        with open(self.__file_path, 'w') as file:
            pass

    def reload(self):
        ''' load objects from a file '''
        if isfile(self.__file_path):
            pass
