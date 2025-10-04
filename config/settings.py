#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python3

import os

API_VERSION = os.environ.get('API_VERSION','R002 @ 2025-09-30')
#
PGSQL_HOST = os.environ.get('PGSQL_HOST', '192.168.0.8')
PGSQL_PORT = os.environ.get('PGSQL_PORT','5432')
PGSQL_USER = os.environ.get('PGSQL_USER', 'admin')
PGSQL_PASSWD = os.environ.get('PGSQL_PASSWD', 'pexco599')
PGSQL_BD = os.environ.get('PGSQL_BD','bd_spcomms')

PGSQL_URL = f"postgresql+psycopg2://{PGSQL_USER}:{PGSQL_PASSWD}@{PGSQL_HOST}:{PGSQL_PORT}/{PGSQL_BD}"

# DEBUG->INFO->ERROR
LOG_LEVEL = "DEBUG"

# API_TESTING
API_TEST_HOST = "127.0.0.1"
API_TEST_PORT = "5300"
API_URL_BASE = f"http://{API_TEST_HOST}:{API_TEST_PORT}/apidatos/"

# Maxima cantidad de lineas de datos leidas por operacion
MAX_CHUNK_SIZE = os.environ.get('MAX_CHUNK_SIZE', 10)


