FROM python:3.9 as build
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir wheel==0.42.0 && pip wheel -r requirements.txt --wheel-dir=/wheels

RUN apt-get update && apt-get install --no-install-recommends -y cron=3.0pl1-162 && apt-get clean && rm -rf /var/lib/apt/lists/*


FROM build as prod
COPY --from=build /wheels /wheels
COPY requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install --no-cache-dir --find-links=/wheels -r requirements.txt

COPY --from=build /app/ /app/
RUN apt-get update && apt-get install --no-install-recommends -y cron=3.0pl1-162 && apt-get clean && rm -rf /var/lib/apt/lists/*
EXPOSE 5000
CMD ["bash", "-c", "gunicorn -b 0.0.0.0:5000 manage:app"]