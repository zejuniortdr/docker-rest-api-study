from python:3.7.4-alpine3.10
MAINTAINER José Luis da Cruz Junior

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

COPY ./api /api
WORKDIR /api
