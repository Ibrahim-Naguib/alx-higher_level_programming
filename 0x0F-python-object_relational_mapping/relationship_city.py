#!/usr/bin/python3
"""Defines City class"""
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    City class represents a city.

    Attributes:
        id (int): The primary key of the city.
        name (str): The name of the city.
        state_id (int): The foreign key referencing the state.
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
