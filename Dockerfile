FROM python:2.7
MAINTAINER Andres Chavez <achavez@rcp.pe>

ADD ./app /srv/www/apidemo
WORKDIR /srv/www/apidemo

RUN apt-get update
RUN apt-get -y install python-dev python-psycopg2
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
