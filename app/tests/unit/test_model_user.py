import pytest
from app.main import db
from app.tests.conftest import (
    new_user,
)


def test_user_model(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the username, email,
        first_name, second_name, last_name,
        second_last_name fields are defined correctly
    """

    assert new_user.username == "johndoe"
    assert new_user.email == "John"
    assert new_user.first_name == "John"
    assert new_user.second_name == "Doe"
    assert new_user.last_name == "Doe"
    assert new_user.second_last_name == "Doele"
    # the password shoud be hashed
    assert new_user.password_hash != "test"


def test_password_hashing(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the password is hashed correctly
    """
    password = "test"
    new_user.password = password

    # the password shoud be hashed
    assert new_user.password_hash != password

    # check password
    assert new_user.check_password(password)

    # wrong password
    assert not new_user.check_password("wrong")
