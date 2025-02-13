FROM python:3.10-slim-buster
LABEL mantainer="Lucas Oliveira"

WORKDIR /app
COPY . /app

EXPOSE 8006

RUN apt-get update \
&& apt-get install -y make \
&& apt-get install -y pkg-config \
&& apt-get install -y gcc \
&& apt-get install -y default-libmysqlclient-dev \
&& apt-get install -y python3-dev

RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
RUN chmod -R 777 /app