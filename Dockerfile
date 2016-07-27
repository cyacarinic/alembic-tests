FROM python:2.7
MAINTAINER Andres Chavez <achavez@rcp.pe>

# Instala dependencias del lenguaje
RUN apt-get update
RUN apt-get -y install python-dev python-psycopg2
RUN pip install --upgrade pip

# Instala requerimientos primero para prevenir cambios en el código
WORKDIR /srv/www/apidemo
ADD ./requirements.txt /srv/www/apidemo

RUN pip install -r requirements.txt

# Agrega el código al final para evitar reconstruir toda la aplicación
ADD ./app /srv/www/apidemo
