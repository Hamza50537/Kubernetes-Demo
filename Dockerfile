FROM python:3.8-slim-buster

ADD app.py /

CMD [ "python3", "./app.py" ]

