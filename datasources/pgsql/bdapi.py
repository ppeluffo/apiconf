#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python
"""
Todas las funciones de la API responde con un diccionario d_res
El campo 'rsp' SIEMPRE ESTA PRESENTE y puede estar en 'OK' o en 'ERR'.
"""
from .models import Usuarios, Configuraciones, Online, RecoverId
from sqlalchemy import text
from config import settings

class ApiBdPgsql:

    def __init__(self, session_factory, logger):
        self.session_factory = session_factory
        self.logger = logger
        
    def ping(self):
        """
        Si el server responde, el ping da True.
        Si no responde, sale por exception.
        """
        self.logger.debug(f"")

        try:
            with self.session_factory() as session:
                session.execute(text("SELECT 1"))
                d_rsp = {'rsp':'OK',
                         'version': settings.API_VERSION,
                         "SQL_HOST": settings.PGSQL_HOST,
                         "SQL_PORT": settings.PGSQL_PORT }
        except Exception as e:
            self.logger.error(f"{e}")
            d_rsp = { 'rsp': 'ERR', 'msg': e}

        return d_rsp

    def get_all_unidades(self):
        """
        Lee toda la tabla de configuraciones y la devuelve tal cual.
        """
        self.logger.debug("")

        try:
            with self.session_factory() as session:
                #unidades_raw = session.query(Configuraciones.unit_id).limit(10).all()
                unidades_raw = session.query(Configuraciones.unit_id).all()
                d_rsp = {'rsp':'OK', 'unidades_raw': unidades_raw }

        except Exception as e:
            self.logger.error(f"{e}")
            d_rsp = { 'rsp': 'ERR', 'msg': e}

        return d_rsp

    def get_config(self, unit_id=None):
        """
        Retorna la configuracion de la unidad 
        """
        self.logger.debug("")

        try:
            with self.session_factory() as session:
                jconfig_raw = session.query(Configuraciones.jconfig).filter(Configuraciones.unit_id == unit_id).first()
                d_rsp = {'rsp':'OK', 'jconfig_raw': jconfig_raw }

        except Exception as e:
            self.logger.error(f"{e}")
            d_rsp = { 'rsp': 'ERR', 'msg': e}

        return d_rsp

    def set_config(self, unit_id=None, jd_config=None):
        """
        Guarda (actualiza) el jdconfig de la unidad
        """
        self.logger.debug("")

        try:
            with self.session_factory() as session:
                recd = session.query(Configuraciones).filter(Configuraciones.unit_id == unit_id).first()
                recd.jconfig = jd_config
                session.commit()
                d_rsp = {'rsp':'OK' }

        except Exception as e:
            self.logger.error(f"{e}")
            d_rsp = { 'rsp': 'ERR', 'msg': e}

        return d_rsp

    def recover_id_from_uid(self, uid=None):
        """
        Retorna la configuracion de la unidad 
        """
        self.logger.debug("")

        try:
            with self.session_factory() as session:
                recoverid_rcd = session.query(RecoverId).filter(RecoverId.uid == uid).first()
                d_rsp = {'rsp':'OK', 'recoverid_rcd': recoverid_rcd }

        except Exception as e:
            self.logger.error(f"{e}")
            d_rsp = { 'rsp': 'ERR', 'msg': e}

        return d_rsp          

    def delete_rcd_by_uid(self, uid=None):
        """
        Borra un registro de recoverid por UID 
        """
        self.logger.debug("")

        try:
            # This gives you a list of ORM objects (DatosHistoricos instances), not rows.
            with self.session_factory() as session:
                session.query(RecoverId).filter(RecoverId.uid == uid).delete(synchronize_session=False)
                session.commit()
                d_rsp = {'rsp':'OK'}

        except Exception as e:
            self.logger.error(f"{e}")
            d_rsp = { 'rsp': 'ERR', 'msg': e}

        return d_rsp  

    def delete_rcd_by_id(self, id=None):
        """
        Borra un registro de recoverid por ID 
        """
        self.logger.debug("")

        try:
            # This gives you a list of ORM objects (DatosHistoricos instances), not rows.
            with self.session_factory() as session:
                session.query(RecoverId).filter(RecoverId.id == id).delete(synchronize_session=False)
                session.commit()
                d_rsp = {'rsp':'OK'}
                
        except Exception as e:
            self.logger.error(f"{e}")
            d_rsp = { 'rsp': 'ERR', 'msg': e}

        return d_rsp 

    def set_id_and_uid(self, id=None, uid=None):
        """
        Guarda (actualiza) un registro uid-id de la tabla recoverid
        """
        self.logger.debug("")

        try:
            with self.session_factory() as session:
                new_rcd = RecoverId(uid=uid, id=id)
                _ = session.add(new_rcd)
                session.commit()
                d_rsp = {'rsp':'OK'}

        except Exception as e:
            self.logger.error(f"{e}")
            d_rsp = { 'rsp': 'ERR', 'msg': e}

        return d_rsp       

   


    

    