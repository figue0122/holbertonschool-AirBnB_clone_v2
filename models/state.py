#!/usr/bin/python3
""" State Module """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm.session import Session
from os import getenv
from models.city import City


class State(BaseModel, Base):
    """ The state class, contains name and relationship to cities """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Getter attribute cities that returns
            the list of City instances"""
            from models import storage
            all_cities = storage.all(City)
            return [city for city in all_cities.values()
                    if city.state_id == self.id]

    def close(self):
        """Close session"""
        Session.close()
