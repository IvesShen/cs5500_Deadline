#http://pythoncentral.io/introductory-tutorial-python-sqlalchemy/
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Pet(Base):
    __tablename__ = 'pet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    color = Column(String(250), nullable=False)
    breed = Column(String(250), nullable=False)


engine = create_engine('sqlite:///sqlalchemy_pet.db')
Base.metadata.create_all(engine)

# class Pet:
#     locations = dict()
#
# 	def __init__(self, petName, petColor, petSize, petType, petBreed, petGender):
# 		self.petName = petName
#         self.petColor = petColor
#         self.petSize = petSize
#         self.petType = petType
#         self.petBreed  = petBreed
#         self.petGender = petGender
#         self.petId = uuid.uuid3(uuid.NAMESPACE_DNS, petName)
#
#     def setLocation(timeStamp, location):
#     	locations[timeStamp] = location
#
#     def getLatestLocation():
#
#     def getLocations(startTimeStamp, endTimeStamp):
