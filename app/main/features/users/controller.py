from flask_restx import Resource
from flask import request
from app.main.features.users.dto import (
    users_api,
    users_model,
)

user_ns = users_api

@user_ns.route('/users')
class UserList(Resource):
    @user_ns.doc('list_of_registered_users')
    @user_ns.marshal_list_with(users_model)
    def get(self):
        """List all registered users"""
        return []