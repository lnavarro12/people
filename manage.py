""" Application Setup """

import os
import unittest
from flask import Flask
from flask_migrate import Migrate

from app.main import create_app, db
from app import blueprint
from app.main.models import * 

app = create_app(os.getenv("RUN_MODE") or "dev")
app.register_blueprint(blueprint)
migrate = Migrate(app, db)

@app.cli.command()
def test():
    """Running unit tests"""
    tests = unittest.TestLoader().discover("app/test", pattern="test*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=app.debug)
