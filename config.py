import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configuración de la base de datos
DATABASE = {
    'host': os.getenv('MYSQL_HOST', 'localhost'),
    'user': os.getenv('MYSQL_USER', 'root'),
    'password': os.getenv('MYSQL_PASSWORD', ''),
    'db': os.getenv('MYSQL_DB', 'anyspa')
}

# Clave secreta para sesiones y seguridad
SECRET_KEY = os.getenv('SECRET_KEY', 'dev_secret_key')
