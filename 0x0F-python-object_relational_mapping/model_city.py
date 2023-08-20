#!/usr/bin/python3
""" This python script creates a declarative base, using it to create
the Base Class 'city' which creates the metadata necessary to map objects
with SQLAlchemy to the database.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State
from sqlalchemy.orm import relationship


class City(Base):
    """ This defines the City class and creates the mapping for it's
        objects to the database.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    state = relationship('State', backref="cities_in_state")
