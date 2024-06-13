""" Application Setup """

import os
import unittest
from dotenv import load_dotenv
from app.main import create_app

load_dotenv()

app = create_app(os.getenv("RUN_MODE") or "dev")
app.app_context().push()


@app.cli.command("run")
def run():
    """Running flask app"""
    app.run(host="0.0.0.0")


@app.cli.command("test")
def test():
    """Running unit tests"""
    tests = unittest.TestLoader().discover("app/test", pattern="test*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == "__main__":
    app.run()
