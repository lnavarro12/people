from flask_restplus import Namespace

class Parametrization:
    """General popularion namespace"""
    api = Namespace("", description="General parametrization model operations")

parametrizations = Parametrization.api
