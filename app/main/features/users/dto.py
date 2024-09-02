""" User DTO """

""" A namespace module contains models and resources declarations"""

from flask_restx import Namespace, fields

users_api = Namespace("users", description="User related operations")

# User DTO for retrieving user information
users_model = users_api.model(
    "User",
    {
        "id": fields.Integer(
            readonly=True, description="The user unique identifier"
        ),
        "username": fields.String(
            required=True, description="The user username"
        ),
        "email": fields.String(required=True, description="The user email"),
        "first_name": fields.String(
            required=True, description="The user first name"
        ),
        "second_name": fields.String(
            required=True, description="The user second name"
        ),
        "last_name": fields.String(
            required=True, description="The user last name"
        ),
        "second_last_name": fields.String(
            required=True, description="The user second last name"
        ),
    },
)

# User DTO for creating a user (includes password field)
user_creation_model = users_api.model(
    "UserCreation",
    {
        "username": fields.String(
            required=True, description="The user username"
        ),
        "email": fields.String(required=True, description="The user email"),
        "first_name": fields.String(
            required=True, description="The user first name"
        ),
        "second_name": fields.String(
            required=False, description="The user second name"
        ),
        "last_name": fields.String(
            required=True, description="The user last name"
        ),
        "second_last_name": fields.String(
            required=False, description="The user second last name"
        ),
        "password": fields.String(
            required=True, description="The user password"
        ),
    },
)
