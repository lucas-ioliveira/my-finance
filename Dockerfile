FROM python:3.10-slim-bullseye
LABEL maintainer="Lucas Oliveira"

WORKDIR /app
COPY . /app

EXPOSE 8001

RUN apt-get update && \
    apt-get install -y make pkg-config gcc libmariadb-dev python3-dev && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
RUN chmod -R 777 /app
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
