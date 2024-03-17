#!/usr/bin/python3
"""Defines City class"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    """
    City class represents a city.

    Attributes:
        id (int): The primary key of the city.
        name (str): The name of the city.
        state_id (int): The foreign key referencing the state.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
