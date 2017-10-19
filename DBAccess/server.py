from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from DB import Pet, Base
from sqlalchemy import create_engine


from flask import Flask
app = Flask(__name__)

engine = create_engine('sqlite:///sqlalchemy_pet.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def index():
    return 'Index Page'

@app.route('/getFirstPet')
def getFirstPet():
    firstPet = session.query(Pet).first()
    return firstPet.name
