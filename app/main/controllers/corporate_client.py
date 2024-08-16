from flask import request
from flask_restplus import Resource
from app.main.dto import parametrizations
from app.main.service import corporate_client as corporate_client_service

corporate_client = parametrizations

@corporate_client.route("/upload/corporate-client")
class CorporateClient(Resource):
    """ This class represents the corporate client resource """
    def post(self):
        """ This method upload a new corporate client """
        return corporate_client_service.upload_corporate_client(request.json)
