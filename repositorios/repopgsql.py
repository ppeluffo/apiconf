#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python3

class RepoPgsql:
    """
    Repositorio que se encarga de consultar la BD Pgsql
    """
    
    def __init__(self, datasource, logger):
        self.datasource = datasource
        self.logger = logger
        
    def ping(self):
        """
        """
        self.logger.debug("")
        return self.datasource.ping()
    
    def get_all_unidades(self):
        """
        """
        self.logger.debug("")
        
        return self.datasource.get_all_unidades()
        
    def get_config(self, unit_id=None):
        """
        """
        self.logger.debug("")
        
        return self.datasource.get_config(unit_id)
    
    def set_config(self, unit_id=None, jd_config=None):
        """
        """
        self.logger.debug("")
        
        return self.datasource.set_config(unit_id, jd_config)
    
    def recover_id_from_uid(self, uid=None):
        """
        """
        self.logger.debug("")
        
        return self.datasource.recover_id_from_uid(uid)
    
    def delete_rcd_by_uid(self, uid=None):
        """
        """
        self.logger.debug("")
        
        return self.datasource.delete_rcd_by_uid(uid)
            
    def delete_rcd_by_id(self, id=None):
        """
        """
        self.logger.debug("")
        
        return self.datasource.delete_rcd_by_id(id)
    
    def set_id_and_uid(self, id=None, uid=None):
        """
        """
        self.logger.debug("")
        
        return self.datasource.set_id_and_uid(id, uid)
    
    