from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from core import db
from model import *
from api import api


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:123456@127.0.0.1:15432"
    db.init_app(app)
    migrate = Migrate(app,db)

    app.register_blueprint(api)

    return app



if __name__ == "__main__":
    app = create_app()

    app.debug = True

    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    manager.run()
