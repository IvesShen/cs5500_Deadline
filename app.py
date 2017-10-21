from flask import Flask
from flask import request, jsonify, session
from os import environ
from flask_sqlalchemy import SQLAlchemy
import json
# import models
# from models import engine, dbsession

__author__ = "Priyank Chaudhary"
__license__ = "MIT"
__credits__ = ["Priyank Chaudhary"]
__version__ = "0.1"
__status__ = "Production"

app = Flask(__name__)
app.config.from_object(environ['APP_SETTINGS'])
db = SQLAlchemy(app)

#TODO: move this to a configuration file.
config = {
    'auth': False  #enable authentication.
}


def is_login_valid():
    return session.get('auth_email') != None


@app.route("/", methods=["GET", "POST", "PUT", "DELETE"])
def index():
    return "Welcome to Pet Project!"


@app.route("/_info")
def info():
    return jsonify({
        "Application":
        "flask-based-pet-project %s" % __version__,
        "Powered By":
        "flask %s, sqlalchemy %s" % (flask.__version__,
                                     sqlalchemy.__version__),
    })


@app.route("/pet", methods=["POST"])
def add_pet():
    """TODO: Docstring for add_pet.
    :returns: TODO

    """


@app.route("/pet/<int:pet_id>", methods=["GET"])
def find_pet_id(pet_id):
    """TODO: Docstring for .

    :pet_id: TODO
    :returns: TODO

    """
    pass


@app.route("/pet/all/", methods=["GET"])
def find_all_known_pets():
    """TODO: Docstring for find_all_known_pets.
    :returns: TODO

    """
    pass

    # @app.route()

    # @app.route("/pet/<int:pet_id>", methods=["PUT"])
    # def update_pet_info(pet_id):
    #     """TODO: Docstring for .

    #     :pet_id: TODO
    #     :returns: TODO

    #     """
    pass


# @app.route("/pet/<int:pet_id>/history", methods=["POST"])

# @app.route("/pet", methods=["POST"])

# @app.route("/pet", methods=["POST"])

# @app.route("/pet", methods=["POST"])

print("pet project v%s" % __version__)
app.secret_key = "some secret"
app.debug = True
app.run()
