#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
meta = MetaData()
Base = declarative_base(metadata=meta)


class State(Base):
    """
    State class to represent states.

    Attributes:
        id (int): The primary key of the state.
        name (str): The name of the state.
        cities (relationship): Relationship to the City class.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state')
