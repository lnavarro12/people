from app.main import db
from app.main.models.users import User

SESSION = db.session


def create_user(data):
    """Create User"""
    # validate if the username already exists
    user = (
        SESSION.query(User)
        .filter(
            User.username == data.get("username"),
            User.email == data.get("email"),
        )
        .first()
    )

    if user:
        raise Exception("User already exists")

    user = User(**data)
    SESSION.add(user)
    SESSION.commit()
    return user
