#!/bin/bash

set -e

echo "Aguardando o banco de dados..."
sleep 5

echo "Aplicando migrações..."
python manage.py migrate --noinput

echo "Iniciando o processo principal..."

exec "$@"
