#!/usr/bin/python3
""" Base Model """

import uuid
import models
from datetime import datetime
from os import getenv
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


if getenv('HBNB_TYPE_STORAGE') == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel:

    """ The base model for other classes in AirBnB clone """
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """ Initialization of the base model """
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.utcnow()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

    def save(self):
        """ Updates the current instance with an updated_at attribute """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """ Deletes the current instance from storage """
        models.storage.delete(self)

    def to_dict(self):
        """ Returns a dictionary of all the keys/values of the instance """
        dict = {}
        dict.update(self.__dict__)
        dict.update({'__class__':
                    str(type(self)).split('.')[-1].split('\'')[0]})
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()
        return dict

    def __str__(self):
        """ Returns a string representation of the instance """
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)
