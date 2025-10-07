#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

from flask_restful import Resource, reqparse
from flask import request

from dependency_injector.wiring import inject, Provide
from container import Container
from servicios.uid2idservice import Uid2idService

class Uid2idResource(Resource):

    @inject
    def __init__(self, service: Uid2idService = Provide[Container.uid2id_service], logger = Provide[Container.logger]):
        self.uid2id_service = service
        self.logger = logger
        
    def get(self):
        """
        Lee de la tabla de recover el id que corresponde al uid
        Se usa cuando un equipo viene con id=DEFAULT
        """
        self.logger.debug("")

        parser = reqparse.RequestParser()
        parser.add_argument('uid',type=str,location='args',required=True)
        args=parser.parse_args()
        uid = args['uid']
        
        d_rsp = self.uid2id_service.recover_id_from_uid(uid)
        status_code = d_rsp.pop('status_code', 500)

        # No mando detalles de los errores en respuestas x seguridad.
        if status_code == 502:
            _ = d_rsp.pop('msg', '')
            d_rsp['msg'] = "SERVICIO NO DISPONIBLE TEMPORALMENTE"
        return d_rsp, status_code

        
    def put(self):
        """
        Crea/actualiza la configuracion de una unidad.
        Recibimos un json con el UID/ID que almacenamos en la BD.
        """
        self.logger.debug("")

        parser = reqparse.RequestParser()
        parser.add_argument('uid',type=str,location='json',required=True)
        parser.add_argument('id',type=str,location='json',required=True)
        args=parser.parse_args()
        uid = args['uid']
        id = args['id']
        
        d_rsp = self.uid2id_service.set_id_and_uid(id, uid)
        status_code = d_rsp.pop('status_code', 500)
        
        # No mando detalles de los errores en respuestas x seguridad.
        if status_code == 502:
            _ = d_rsp.pop('msg', '')
            d_rsp['msg'] = "SERVICIO NO DISPONIBLE TEMPORALMENTE"
        return d_rsp, status_code
    

 