from flask import request
from flask_restplus import Resource
from app.main.dto import parametrizations
from app.main.service import client_population as client_population_service

client_population = parametrizations


@client_population.route("/upload/client-population")
class ClientPopulation(Resource):
    def post(self):
        return client_population_service.upload_client_population(request.json)

