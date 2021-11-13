#!/usr/bin/python3
"""A module containing the base model for all data sets.
"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Represents the base class for all data sets.
    """
    def __init__(self, *args, **kwargs):
        """Initializes a new instance of the BaseModel.

        Args:
            *args (tuple): Ignored.
            kwargs: A dictionary of attribute keys-value pairs.
        """
        from models import storage
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
            # self.updated_at = datetime.now()
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Creates a string representation of a BaseModel instance.

        Returns:
            str: A string representation of a BaseModel instance.
        """
        res = '[{}] ({}) {}'.format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )
        return res

    def save(self):
        """Saves the changes made to this BaseModel instance.
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
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
        res['__class__'] = self.__class__.__name__
        return res
