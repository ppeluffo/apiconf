#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

from flask_restful import Resource, reqparse
from dependency_injector.wiring import inject, Provide
from container import Container
from servicios.unidadesservice import UnidadesService

class UnidadesResource(Resource):

    @inject
    def __init__(self, service: UnidadesService = Provide[Container.unidades_service], logger = Provide[Container.logger]):
        self.unidades_service = service
        self.logger = logger
        
    def get(self):
        """
        Devuelve una lista con todas las unidades configuradas
        """
        self.logger.debug("")

        d_rsp = self.unidades_service.get_all_unidades()

        if d_rsp.get('rsp','ERR') == 'OK':
            return d_rsp,200
        else:
            return d_rsp, 500

