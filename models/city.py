#!/usr/bin/python3
""" City Module """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
<<<<<<< HEAD
=======

>>>>>>> 9ef57b8c2da398cc5788cf3c1f49827a0947306a

class City(BaseModel, Base):

    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", backref="city", cascade="all, delete-orphan")
