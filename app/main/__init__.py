""" Application Setup """

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from flask_bcrypt import Bcrypt
import redis
from configuration.environment import config_by_name

db = SQLAlchemy()
cache = Cache()
flask_bcrypt = Bcrypt()


def create_app(config_name):
    """Creating flask object"""
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    # Initialize extensions
    #cache.init_app(app)
    db.init_app(app)
    return app
