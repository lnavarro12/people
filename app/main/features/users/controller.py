from flask_restx import Resource
from flask import request
from app.main.features.users.dto import (
    users_api,
    users_model,
    user_creation_model,
)
from app.main.features.users.service import (
    create_user,
)

user_ns = users_api


@user_ns.route("/")
class User(Resource):
    @user_ns.doc("create a new user")
    @user_ns.expect(user_creation_model, validate=True)
    @users_api.marshal_with(users_model, code=201)
    def post(self):
        """Create User"""
        data = request.json
        return create_user(data)
