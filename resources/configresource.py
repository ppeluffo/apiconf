#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

from flask_restful import Resource, reqparse
from flask import request

from dependency_injector.wiring import inject, Provide
from container import Container
from servicios.configservice import ConfigService

class ConfigResource(Resource):

    @inject
    def __init__(self, service: ConfigService = Provide[Container.config_service], logger = Provide[Container.logger]):
        self.config_service = service
        self.logger = logger
        
    def get(self):
        """
        Lee la configuracion de un equipo de la SQL
        En la BS almacenamos json.(strings)
        Retornamos un json.
        """
        self.logger.debug("")

        parser = reqparse.RequestParser()
        parser.add_argument('unit',type=str,location='args',required=True)
        args=parser.parse_args()
        unit_id = args['unit']

        d_rsp = self.config_service.get_config(unit_id)

        return d_rsp, 200
        
    def post(self):
        """
        Crea/actualiza la configuracion de una unidad.
        Recibimos un json que almacenamos.
        No lo chequeamos !!!
        """
        self.logger.debug("")

        parser = reqparse.RequestParser()
        parser.add_argument('unit',type=str,location='args',required=True)
        args=parser.parse_args()
        unit_id = args['unit']
        #
        d_config = request.get_json()

        d_rsp = self.config_service.set_config(unit_id, d_config)

        return d_rsp, 200
    

