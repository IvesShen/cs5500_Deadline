#encoding: utf-8

import datetime
import jwt
import uuid
from functools import wraps

from flask import Flask
from flask import g
from flask import json
from flask import jsonify
from flask import make_response
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for

from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

import config
from exts import db
from models import Pet
from models import User


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def hello_world():
	'''
	hello_world.
	'''
    return 'Hello World!'


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(public_id = data['public_id']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)
    return decorated


@app.route('/login')
def login():

    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW.Authenticate' : 'Basic realm="Login required!"'})

    user = User.query.filter_by(name = auth.username).first()

    if not user:
        return make_response('Could not verify', 401, {'WWW.Authenticate' : 'Basic realm="Login required!"'})

    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes = 30)}, app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('UTF-8')})

    return make_response('Could not verify', 401, {'WWW.Authenticate': 'Basic realm="Login required!"'})


@app.route('/user', methods = ['POST'])
@token_required
def create_user(current_user):
	'''
	Create user in DB.
	current_user: current user data object.
	'''
    if not current_user.admin:
        return jsonify({'message': 'Cannot perform that function!'})

    data = request.get_json()

    hashed_password = generate_password_hash(data['password'], method = 'sha256')

    new_user = User(public_id = str(uuid.uuid4()), name = data['name'], password = hashed_password, admin = False)
    addItemToDB(new_user)

    return jsonify({'message': 'New user created!'})


@app.route('/user/promote/<public_id>', methods = ['PUT'])
@token_required
def promote_user(current_user, public_id):
	'''
	Promote user to admin user.
	current_user: current user data object.
	public_id: user public ID.
	'''
    if not current_user.admin:
        return jsonify({'message': 'Cannot perform that function!'})

    user = User.query.filter_by(public_id = public_id).first()

    if not user:
        return jsonify({'message': 'No user found!'})

    user.admin = True
    db.session.commit()

    return jsonify({'message' : 'The user has been promoted'})


@app.route('/user', methods = ['GET'])
@token_required
def get_all_users(current_user):
	'''
	Get all users.
	current_user: current user data object.
	'''
    if not current_user.admin:
        return jsonify({'message': 'Cannot perform that function!'})

    users = User.query.all()

    output = []
    for user in users:
        user_data = {'public_id': user.public_id, 'name': user.name, 'password': user.password, 'admin': user.admin}
        output.append(user_data)

    return jsonify({'users' : output})


@app.route('/user/<public_id>', methods = ['GET'])
@token_required
def get_one_user(current_user, public_id):
	'''
	Get user given user public ID.
	current_user: current user data object.
	public_id: user public ID.
	'''
    if not current_user.admin:
        return jsonify({'message': 'Cannot perform that function!'})

    flag, user, errorMessage = getUser(current_user, public_id)
    if flag is False:
    	return errorMessage
    else:
    	user_data = {'public_id': user.public_id, 'name': user.name, 'password': user.password, 'admin': user.admin}
    	return jsonify({'user' : user_data})


@app.route('/user/<public_id>', methods = ['PUT'])
@token_required
def update_user(current_user, public_id):
	'''
	Updat user information.
	current_user: current user data object.
	public_id: user public ID.
	'''
    flag, user, errorMessage = getUser(current_user, public_id)
    if flag is False:
    	return errorMessage
    else:
    	new_name = json.loads(request.data)
	    user.name = new_name.get('name')
	    db.session.commit()
    	return jsonify({'message' : 'The user has been updated'})


@app.route('/user/<public_id>', methods = ['DELETE'])
@token_required
def delete_user(current_user, public_id):
	'''
	Delete user according to user public ID.
	current_user: current user data object.
	public_id: user public ID.
	'''
    if not current_user.admin:
        return jsonify({'message': 'Cannot perform that function!'})

    flag, user, errorMessage = getUser(current_user, public_id)
    if flag is False:
    	return errorMessage
    else:
    	deleteItemInDB(user)
    	return jsonify({'message' : 'The user has been deleted'})

def getUser(public_id):
	'''
	Get user from DB according to user public ID.
	public_id: user public ID.
	'''
	user = User.query.filter_by(public_id = public_id).first()

    if not user:
        return False, None, jsonify({'message': 'No user found!'})
    else:
    	return True, user, None


@app.route('/pet', methods = ['POST'])
@token_required
def create_pet(current_user):
	'''
	Create pet.
	current_user: current user data object.
	'''
    data = request.get_json()

    new_pet = Pet(name = data['name'], owner_id = current_user.id)
    addItemToDB(new_pet)

    return jsonify({'message': "Pet created!"})


@app.route('/pet', methods = ['GET'])
@token_required
def get_all_pets(current_user):
	'''
	Get all pets.
	current_user: current user data object.
	'''
    pets = Pet.query.filter_by(owner_id = current_user.id).all()

    output = []
    for pet in pets:
        pet_data = {'id': pet.id, 'name': pet.name}
        output.append(pet_data)

    return jsonify({'pets' : output})


@app.route('/pet/<pet_id>', methods = ['GET'])
@token_required
def get_one_pet(current_user, pet_id):
	'''
	Create one pet according to pet ID.
	current_user: current user data object.
	pet_id: pet ID.
	'''
    flag, pet, errorMessage = getPet(pet_id, current_user.id)
    if flag is False:
    	return errorMessage
    else:
	    pet_data = {'id': pet.id, 'name': pet.name}
	    return jsonify(pet_data)


@app.route('/pet/<pet_id>', methods = ['PUT'])
@token_required
def update_pet(current_user, pet_id):
	'''
	Update pet information.
	current_user: current user data object.
	pet_id: pet ID.
	'''
	flag, pet, errorMessage = getPet(pet_id, current_user.id)
    if flag is False:
    	return errorMessage
    else:
	    new_name = json.loads(request.data)
	    pet.name = new_name.get('name')
	    db.session.commit()
	    return jsonify({'message': 'Pet updated!'})


@app.route('/pet/<pet_id>', methods = ['DELETE'])
@token_required
def delete_pet(current_user, pet_id):
	'''
	Delete pet according to pet ID.
	current_user: current user data object.
	pet_id: pet ID.
	'''
    flag, pet, errorMessage = getPet(pet_id, current_user.id)
    if flag is False:
    	return errorMessage
    else:
	    deleteItemInDB(pet)
	    return jsonify({'message': "Pet deleted!"})


def getPet(pet_id, current_user_id):
	'''
	Get pet from DB according to pet_id and current_user_id.
	pet_id: pet ID.
	current_user_id: current user ID.
	'''
	pet = Pet.query.filter_by(id = pet_id, owner_id = current_user_id).first()

    if not pet:
        return False, None, jsonify({'message': "No Pet found"})
    else:
    	return True, pet, None


def addItemToDB(item):
	'''
	Add item to DB.
	item: new user or new pet.
	'''
	db.session.add(item)
    db.session.commit()


def deleteItemInDB(item):
	'''
	Delete item in DB.
	item: existing user or existing pet.
	'''
	db.session.delete(item)
    db.session.commit()


if __name__ == '__main__':
    app.run(debug = True)
