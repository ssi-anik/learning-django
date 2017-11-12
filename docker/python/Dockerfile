FROM python:3.6.3

RUN apt-get update && apt-get install -y libmysqlclient-dev

WORKDIR /var/www/html

EXPOSE 9000

ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt