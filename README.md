# Flask Application

## Getting Started

### Prerequisites

Ensure you have Docker installed and running on your machine.

### Running the Application

1. **Build and Start the Docker Containers**

   Use Docker Compose to build and start your containers:

   ```bash
   docker-compose up --build

2. **Run Flask Migrations**

    - Access the Docker Container: To run commands inside the Flask application container, first access the container shell
    ```bash
    docker exec -it "ID CONTAINER" /bin/bash

    - Set the FLASK_APP Environment Variable: Inside the container, set the FLASK_APP environment variable to point to your Flask application:

    ```bash
    export FLASK_APP=manage.py

    - Initialize Migrations (only if not done before):

    ```bash
    flask db init

    - Generate Migrations:
    ```bash
    flask db migrate -m "Migration message"

    - Apply Migrations:
    ```bash
    flask db upgrade





