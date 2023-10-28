#!/usr/bin/python3
""" State Module for HBNB project """
from models import storage
from os import getenv
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="delete")
    else:
        @property
        def cities(self):
            """returns list of City instances upon state_id"""
            cities_list = []
            for obj in list(storage.all(City).values()):
                if obj.state_id == self.id:
                    cities_list.append(obj)
            return cities_list
