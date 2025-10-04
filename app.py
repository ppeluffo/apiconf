#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python
"""
API REST para acceder a los servicios de REDIS del servidor de comunicaciones

"""

import logging
from config import settings

from resources import helpresource
from resources import pingresource
from resources import unidadesresource
from resources import configresource
from resources import uid2idresource

from container import Container

from flask import Flask
from flask_restful import Api

from utilidades.login_config import configure_logger

def create_app(gunicorn: bool = False):

    app = Flask(__name__)
    api = Api(app)

    container = Container()

    # Sobrescribir logger según modo
    container.logger.override(configure_logger("api-redis", gunicorn=gunicorn))

    container.init_resources()
    container.wire(modules=[__name__])

    api.add_resource( pingresource.PingResource, '/apiconf/ping')
    api.add_resource( helpresource.HelpResource, '/apiconf/help')
    api.add_resource( unidadesresource.UnidadesResource, '/apiconf/unidades')
    api.add_resource( configresource.ConfigResource, '/apiconf/config')
    api.add_resource( uid2idresource.Uid2idResource, '/apiconf/uid2id')

    return app

# Lineas para cuando corre en gurnicorn
if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app = create_app(gunicorn=True)
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    app.logger.info(f'Starting APICONF: PGSQL_HOST={settings.PGSQL_HOST}, PGSQL_PORT={settings.PGSQL_PORT}')


# Lineas para cuando corre en modo independiente
if __name__ == '__main__':
    app = create_app(gunicorn=False)
    app.run(host='0.0.0.0', port=5200, debug=True)

