import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), ForeignKey('user.id'))
    character_name = Column(String(250))
    planet_name = Column(String(250))
    vehicle_name = Column(String(250))
    person = relationship(User) # ???

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), ForeignKey('favorites.character_name'))
    mass = Column(Integer)
    height = Column(String(250))
    favorites = relationship(Favorites) # ???

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), ForeignKey('favorites.planet_name'))
    population = Column(Integer)
    terrain = Column(String(250))
    # person = relationship(User) # ???

class Vechicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), ForeignKey('favorites.planet_name'))
    speed = Column(Integer)
    manufacturer = Column(String(250))
    # person = relationship(User) # ???

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
