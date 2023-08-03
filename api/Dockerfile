FROM python:3.8

ENV PYTHONNUNBUFFERED 1

COPY requirements.txt /requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD . /app
WORKDIR /app
