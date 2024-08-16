""" Application Setup """

import os
import unittest
from dotenv import load_dotenv
from flask_script import Manager
from app.main import create_app
from app import blueprint

load_dotenv()

app = create_app(os.getenv("RUN_MODE") or "dev")
app.register_blueprint(blueprint)
app.app_context().push()
manager = Manager(app)


@manager.command
def run():
    """Running flask app"""
    app.run(host="0.0.0.0")


@manager.command
def test():
    """Running unit tests"""
    tests = unittest.TestLoader().discover("app/test", pattern="test*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == "__main__":
    manager.run()
