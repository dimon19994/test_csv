FROM python:3.10.7-slim-buster

WORKDIR /usr/src/app

COPY . /usr/src/app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt



CMD ["python", "runserver.py"]