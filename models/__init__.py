#!/usr/bin/python3
"""Modules for working with data sets.
"""
from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
