import os
from flask_restx import Api
from flask import Blueprint
from flask_cors import CORS
from app.main.features.users.controller import user_ns

# Modular Applications with Blueprints 
blueprint = Blueprint("api", __name__)
CORS(blueprint)

api = Api(
    blueprint,
    prefix=os.getenv("URL_MS") + os.getenv("API_VERSION"),
    title="Password Manager",
    version=os.getenv("VERSION"),
    description="Password generator, manager and library",
)

user_ns = api.add_namespace(user_ns)

