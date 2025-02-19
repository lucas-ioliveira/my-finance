#!/bin/bash

echo "Aguardando o banco de dados..."
sleep 5  

echo "Aplicando migrações..."
python manage.py migrate

echo "Iniciando o servidor Django..."
python manage.py runserver 0.0.0.0:8006