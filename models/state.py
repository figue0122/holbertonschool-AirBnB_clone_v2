#!/usr/bin/python3
""" State Module """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models

class State(BaseModel, Base):
    """ The state class, contains name and relationship to cities """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if models.storage_t == 'db':
        cities = relationship("City", backref="state", cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            """ Getter for cities in the file storage """
            return [city for city in models.storage.all(City).values() if city.state_id == self.id]
