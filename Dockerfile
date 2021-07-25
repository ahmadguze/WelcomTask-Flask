From python:3.8

WORKDIR /docker-flask-test

add . /docker-flask-test

Run  pip install -r requirements.txt

EXPOSE 5000

Cmd ["python", "app.py"]


