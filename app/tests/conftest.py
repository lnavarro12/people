""" fixtures for testing """

import pytest
from app.main import db
from app.main.models import User

SESSION = db.session


@pytest.fixture(scope="module")
def db_session():
    """Fixture to create a new database session"""
    session = SESSION
    yield session
    session.rollback()
    session.close()


@pytest.fixture
def new_user():
    """Fixture to create a new user"""
    return User(
        username="johndoe",
        first_name="John",
        second_name="Doe",
        last_name="Doe",
        second_last_name="Doele",
        email="John",
        password="test",
    )
