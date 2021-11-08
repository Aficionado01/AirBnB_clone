#!/usr/bin/python3
"""A module containing the base model for all data sets.
"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Represents the base class for all data sets.
    """
    id: str
    created_at: datetime
    updated_at: datetime

    def __init__(self) -> None:
        """Initializes a new instance of the BaseModel.
        """
        self.id = str(uuid4())
        time = datetime.now()
        self.created_at = time
        self.updated_at = time

    def __str__(self) -> str:
        """Creates a string representation of a BaseModel instance.

        Returns:
            str: A string representation of a BaseModel instance.
        """
        return '[{s}] ({}) {}'.format(self.__class__, self.id, self.__dict__)

    def save(self) -> None:
        """Saves the changes made to this BaseModel instance.
        """
        self.updated_at = datetime.now()

    def to_dict(self) -> dict:
        """Returns a dictionary consisting of this BaseModel instance's
        attibute keys and values.

        Returns: A dictionary of the attribute key-value pairs.
        """
        res = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                res[key] = value.isoformat()
            else:
                res[key] = value
        res['__class__'] = str(self.__class__)
        return res
