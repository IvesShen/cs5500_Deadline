#encoding: utf-8

from flask_migrate import Migrate
from flask_migrate import MigrateCommand
from flask_script import Manager

from exts import db
from models import Pet
from models import User
from msd5500_project import app

'''
Initialize and start the Manager.
'''

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
    manager.run()