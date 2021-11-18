#!/usr/bin/python3
"""defines State class"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """defines class attributes for State class
    Args:
        Base: base class
    Attributes:
        id: state id
        name: state name
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=Fals)
    name = Column(String(128), nullable=False)
