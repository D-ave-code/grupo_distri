FROM python:3-slim-buster
WORKDIR /app
COPY . /app

RUN pip install -r requerimientos.txt

CMD flask run --port 7001 --host 0.0.0.0