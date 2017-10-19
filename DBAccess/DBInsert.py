from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from DB import Pet, Base

engine = create_engine('sqlite:///sqlalchemy_pet.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Insert a Person in the person table
new_pet = Pet(name='pp', color='white', breed='dog')
session.add(new_pet)
session.commit()
