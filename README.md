# Flask Application

## Getting Started

### Prerequisites

Ensure you have Docker installed and running on your machine.

### Running the Application

1. **Build and Start the Docker Containers**

   Use Docker Compose to build and start your containers:

   ```bash
   docker-compose up --build
   ```

2. **Run Flask Migrations**

    - Access the Docker Container: To run commands inside the Flask application container, first access the container shell
    ```bash
    docker exec -it "ID CONTAINER" /bin/bash
    ```

    - Set the FLASK_APP Environment Variable: Inside the container, set the FLASK_APP environment variable to point to your Flask application:

    ```bash
    export FLASK_APP=manage.py
    ```

    - Initialize Migrations (only if not done before):

    ```bash
    flask db init
    ```

    - Generate Migrations:
    ```bash
    flask db migrate -m "Migration message"
    ```

    - Apply Migrations:
    ```bash
    flask db upgrade
    ```

## Implement pytest

*pytest* is a test framework for Python used to write, organize, and run test cases. After setting up your basic test structure, pytest makes it easy to write tests and provides a lot of flexibility for running the tests. pytest satisfies the key aspects of a good test environment:

- tests are fun to write
- tests can be written quickly by using helper functions (fixtures)
- tests can be executed with a single command
- tests run quickly

*you may use unit tests to test:*

- Database models (often defined in models.py)
- Utility functions (for example, server-side validation checks) that your view functions call

base on:
- https://testdriven.io/blog/flask-pytest/
- https://coderpad.io/blog/development/a-guide-to-database-unit-testing-with-pytest-and-sqlalchemy/





