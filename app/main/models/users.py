
""" User Model """
from app.main import db, flask_bcrypt
from sqlalchemy.orm import Mapped

class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = db.Column(db.Integer, primary_key=True)
    first_name: Mapped[str] = db.Column(db.String(80), nullable=False)
    second_name: Mapped[str] = db.Column(db.String(80), nullable=True)
    last_name: Mapped[str] = db.Column(db.String(80), nullable=False)
    second_last_name: Mapped[str] = db.Column(db.String(80), nullable=True)
    username: Mapped[str] = db.Column(db.String(80), unique=True, nullable=False)
    password_hash: Mapped[str] = db.Column(db.String(100))

    @property
    def password(self):
        """Prevent password from being accessed"""
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        """Check hashed password."""
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username}>"
