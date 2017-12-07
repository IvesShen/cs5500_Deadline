#encoding: utf-8

from datetime import datetime

from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from exts import db

'''
Define database data model.
'''

class User(db.Model):
	"""User data model.

    User data model includes 5 fields.
    id: user ID.
    public_id: public user ID.
    name: user name.
    password: user password.
    admin: is admin user?
    """
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    public_id = db.Column(db.String(50), unique = True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)


class Pet(db.Model):
	"""Pet data model.

    Pet data model includes 3 fields.
    id: pet ID.
    name: pet name.
    owner_id: pet owner ID. 
    """
    __tablename__ = 'pet'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(100))
    owner_id = db.Column(db.Integer)
