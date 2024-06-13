""" configurations settings per environment """

import os
import dataclasses
from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))


@dataclasses.dataclass
class Config:
    """Base configuration"""

    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    DEBUG = False


@dataclasses.dataclass
class DevelopmentConfig(Config):
    """Development configuration"""

    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    HOST = os.getenv("POSTGRES_HOST")
    USER = os.getenv("POSTGRES_USER")
    PASSWORD = os.getenv("POSTGRES_PASSWORD")
    DBPORT = os.getenv("DBPORT")
    DATABASE = os.getenv("POSTGRES_DATABASE")
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{USER}:{PASSWORD}@{HOST}:{DBPORT}/{DATABASE}"
    )

    CACHE_TYPE = os.getenv('CACHE_TYPE')
    CACHE_REDIS_HOST = os.getenv('CACHE_REDIS_HOST')
    CACHE_REDIS_PORT = os.getenv('CACHE_REDIS_PORT')
    CACHE_REDIS_DB = os.getenv('CACHE_REDIS_DB')

@dataclasses.dataclass
class TestingConfig(Config):
    """Testing configuration"""

    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    HOST = None
    USER = None
    PASSWORD = None
    DBPORT = None
    DATABASE = None
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{USER}:{PASSWORD}@{HOST}:{DBPORT}/{DATABASE}"
    )


@dataclasses.dataclass
class ProductionConfig(Config):
    """Production configuration"""

    DEBUG = False
    HOST = None
    USER = None
    PASSWORD = None
    DBPORT = None
    DATABASE = None
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{USER}:{PASSWORD}@{HOST}:{DBPORT}/{DATABASE}"
    )


config_by_name = {
    "dev": DevelopmentConfig,
    "test": TestingConfig,
    "prod": ProductionConfig,
}

key = Config.SECRET_KEY
