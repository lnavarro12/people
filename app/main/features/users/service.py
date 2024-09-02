from app.main import db
from app.main.models.users import User


def create_user(data):
    return User(**data)
