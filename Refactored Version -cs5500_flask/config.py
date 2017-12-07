#encoding: utf-8

import os

'''
Configuration for the server and database.
'''

DEBUG = True

SECRET_KEY = os.urandom(24)

DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'b94873d094798f'
PASSWORD = '3fad4ca6'
HOST = 'us-cdbr-iron-east-05.cleardb.net'
PORT = '3306'
DATABASE = 'heroku_18840c90bafad32'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = True


# DIALECT = 'mysql'
# DRIVER = 'mysqldb'
# USERNAME = 'root'
# PASSWORD = 'root'
# HOST = '127.0.0.1'
# PORT = '3306'
# DATABASE = 'db_msd'
#
# SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)
#
# SQLALCHEMY_TRACK_MODIFICATIONS = True