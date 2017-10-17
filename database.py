import os
import sys
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class PetShop(Base):
    __tablename__ = 'pet_shop'

    id = Column(Integer, primary_key = True)
    category = Column(Integer, nullable = False)
    lon = Column(Float, nullable = False)
    lat = Column(Float, nullable = False)
    name = Column(String(100), nullable = False)
    description = Column(String(1000))
    url = Column(String(100))
    pet_id = Column(Integer, ForeignKey('pet.id'))
    pet = relationship(Pet)

class Pet(Base):
    __tablename__ = 'pet'

    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)
    pet_type = Column(String(250), nullable = False)
    picture = Column(String(250))
    age = Column(Integer)

engine = create_engine('postgres://mitekazufcmltz:e18d2563c545e9e1ed4f8eb650e17fc3ab8e39e9872a9f789bc05357fb142adf@ec2-54-83-205-71.compute-1.amazonaws.com:5432/dk0jn7si7ukph')
Base.metadata.create_all(engine)
