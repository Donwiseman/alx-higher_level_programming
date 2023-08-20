#!/usr/bin/python3
""" This python script creates a declarative base, using it to create
the Base Class 'State' which creates the metadata necessary to map objects
with SQLAlchemy to the database.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """ This defines the State class and creates the mapping for it's
        objects to the database.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
