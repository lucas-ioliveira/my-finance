FROM python:3.12-slim-bullseye
LABEL mantainer="Lucas Oliveira"

WORKDIR /app
COPY . /app

EXPOSE 8005

RUN apt-get update && \
    apt-get install -y make pkg-config gcc default-libmysqlclient-dev python3-dev && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

RUN chmod -R 777 /app

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
