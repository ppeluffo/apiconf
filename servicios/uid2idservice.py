#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

import json

class Uid2idService:
    """
    """
    def __init__(self, repositorio, logger):
        self.repo = repositorio
        self.logger = logger

    def recover_id_from_uid(self, uid=None):
        """
        """
        self.logger.debug("")
        
        d_rsp = self.repo.recover_id_from_uid(uid)

        if d_rsp.get('rsp','ERR') == 'OK':
            recoverid_rcd = d_rsp['recoverid_rcd']
            # Por si la BD no devolvio nada
            if recoverid_rcd is None:
                id = None
            else:
                id = recoverid_rcd.id

            d_rsp = { 'rsp':'OK', 'uid':uid, 'id':id}

        return d_rsp
    
    def set_id_and_uid(self, id=None, uid=None):
        """
        Borra todos los registros de recoverid que existan con el UID
        Idem con el ID
        Inserta un nuevo registro.
        """
        self.logger.debug("")
        
        # Borro todos los registros con el UID
        d_rsp = self.repo.delete_rcd_by_uid(uid)
        if d_rsp.get('rsp','ERR') == 'OK':
            # Borro todos los registros con el ID
            d_rsp = self.repo.delete_rcd_by_id(id)
            if d_rsp.get('rsp','ERR') == 'OK':
                # Inserto un nuevo registro UID/ID
                d_rsp = self.repo.set_id_and_uid(id, uid)

        return d_rsp
