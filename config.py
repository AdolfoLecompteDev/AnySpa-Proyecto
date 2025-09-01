import os
from dotenv import load_dotenv

load_dotenv()

# Rutas relativas para proteger la base de datos

DATABASE = {
    'host': os.getenv('MYSQL_HOST'),
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'db': os.getenv('MYSQL_DB')
}

SECRET_KEY = os.getenv('SECRET_KEY')