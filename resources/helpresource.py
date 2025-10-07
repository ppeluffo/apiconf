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
            'GET /apiconf/config':' Retorna la configuracion de la unidad solicitada',
            'POST /apiconf/config':'Crea/Actualiza la configuracion de la unidad indicada',
            'GET /apiconf/unidades':' Retorna una lista con todas las unidades configuradas',
            'GET /apiconf/uid2id':'Lee un id que corresponde al uid pasado como parametro',
            'PUT /apiconf/uid2id':'Actualiza la configuracion de comunicaciones de la unidad indicada',
        }
        return {'d_options': d_options} , 200