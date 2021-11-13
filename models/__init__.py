#!/usr/bin/python3
"""Modules for working with data sets.
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
"""A unique FileStorage instance for all models.
"""
storage.reload()
