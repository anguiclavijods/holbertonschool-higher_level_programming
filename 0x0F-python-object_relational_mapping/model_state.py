#!/usr/bin/python3
"""
Module that connect a database
with port 3306 and create table
as syntax of SQLalchemy
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


# connect database
# engine = create_engine("mysql://root:root@localhost:3306/db")

# super class that permit of mapping of class children
Base = declarative_base()


# inherits
class State(Base):
    __tablename__ = 'states'
    # attributes
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

# connect and created table
# Base.metadata.create_all(engine)
