FROM python:3.7-alpine
MAINTAINER Siraj

ENV PYTHONDJANGOWEB 1
COPY ./requirements.txt /requirements.txt
RUN pip install --trusted-host pypi.org -r  /requirements.txt


RUN adduser -D user
USER user