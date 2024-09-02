# Base stage for building the wheels and running tests
FROM python:3.9 as build

WORKDIR /app
COPY . /app

# Install dependencies and create wheels
RUN pip install --no-cache-dir wheel==0.42.0 pytest==7.4.2 \
    && pip wheel -r requirements.txt --wheel-dir=/wheels

# Run pytest tests
#RUN pytest --maxfail=1 --disable-warnings

# Install cron
RUN apt-get update && apt-get install --no-install-recommends -y cron=3.0pl1-162 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Production stage
FROM build as prod

# Copy wheels and install dependencies
COPY --from=build /wheels /wheels
COPY requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install --no-cache-dir --find-links=/wheels -r requirements.txt

# Copy application code
COPY --from=build /app/ /app/

# Install cron again (optional, if needed in prod stage)
RUN apt-get update && apt-get install --no-install-recommends -y cron=3.0pl1-162 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

EXPOSE 5000

# Run the application
CMD ["bash", "-c", "gunicorn -b 0.0.0.0:5000 manage:app"]