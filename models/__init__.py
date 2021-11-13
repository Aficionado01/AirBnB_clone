#!/usr/bin/python3
"""Modules for working with data sets.
"""
import models.engine.file_storage as file_storage


storage = file_storage.FileStorage()
storage.reload()
