FROM python:3.7.4
MAINTAINER José Luis da Cruz Junior

ENV PYTHONUNBUFFERED 1
ENV TZ 'America/Sao_Paulo'

COPY ./api /api
WORKDIR ./api

RUN pip install --upgrade pip && pip install -r ${REQUIREMENTS:-requirements/requirements-dev.txt}

COPY ./utils/entrypoint.sh /entrypoint.sh
COPY ./utils/wait-for-mysql.py /wait-for-mysql.py
ENTRYPOINT ["/entrypoint.sh"]
