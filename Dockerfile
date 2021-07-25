From python:3.8

WORKDIR /docker-flask-test

add . /docker-flask-test

Run  pip install -r requirements.txt

Cmd ["python", "app.py"]


