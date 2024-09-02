""" User DTO """
""" A namespace module contains models and resources declarations"""

from flask_restx import Namespace, Resource, fields

users_api = Namespace('users', description='User related operations')

users_model = users_api.model('User', {
    'id': fields.Integer(readonly=True, description='The user unique identifier'),
    'username': fields.String(required=True, description='The user username'),
    'email': fields.String(required=True, description='The user email'),
    'first_name': fields.String(required=True, description='The user first name'),
    'second_name': fields.String(required=True, description='The user second name'),
    'last_name': fields.String(required=True, description='The user last name'),
    'second_last_name': fields.String(required=True, description='The user second last name'),
    'password': fields.String(required=True, description='The user password'),
})