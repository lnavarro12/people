import os
from flask_restx import Api
from flask import Blueprint
from flask_cors import CORS

blueprint = Blueprint("api", __name__)
CORS(blueprint)

api = Api(
    blueprint,
    prefix=os.getenv("URL_MS") + os.getenv("API_VERSION"),
    title="Password Manager",
    version=os.getenv("VERSION"),
    description="Password generator, manager and library",
)

