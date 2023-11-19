#!/usr/bin/python3
"""
contains the class definition of a City
and an instance Base = declarative_base()
"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Defines class City
    """
    __tablename__ = "cities"
    id = Column(Integer, nullable=False, primary_key=True)  # autoincrements
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
