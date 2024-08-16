import os
from flask_restplus import Api
from flask import Blueprint
from flask_cors import CORS

from app.main.controllers.client_population import client_population
from app.main.controllers.corporate_client import corporate_client

blueprint = Blueprint("api", __name__)
CORS(blueprint)

api = Api(
    blueprint,
    prefix=os.getenv("URL_MS") + os.getenv("API_VERSION"),
    title="Parameterization Module",
    version=os.getenv("VERSION"),
    description="Parameterization Module",
)

api.add_namespace(client_population)
api.add_namespace(corporate_client)
