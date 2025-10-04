#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

from flask_restful import Resource, reqparse
from dependency_injector.wiring import inject, Provide
from container import Container

class HelpResource(Resource):

    @inject
    def __init__(self, logger = Provide[Container.logger]):
        self.logger = logger

    def get(self):
        ''' Retorna la descripcion de los metodos disponibles
        '''
        self.logger.debug("")
        
        d_options = {
            'GET /apiconf/versiones':'Retorna una lista con todas las versiones que se manejan',
            'GET /apiconf/template':'Retorna el template de la version indicada',
            'GET /apiconf/config':' Retorna la configuracion de la unidad solicitada',
            'POST /apiconf/config':'Crea/Actualiza la configuracion de la unidad indicada',
            'GET /apiconf/unidades':' Retorna una lista con todas las unidades configuradas',
            'POST /apiconf/commsidparams':'Actualiza la configuracion de comunicaciones de la unidad indicada',
        }
        return {'rsp': 'OK', 'd_options': d_options} , 200