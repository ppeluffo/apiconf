#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

import json

class ConfigService:
    """
    """
    def __init__(self, repositorio, logger):
        self.repo = repositorio
        self.logger = logger

    def get_config(self, unit_id=None):
        """
        """
        self.logger.debug("")
        
        d_rsp = self.repo.get_config(unit_id)
    
        if d_rsp.get('status_code',0) == 200:
            # La BD devuelve una tupla !!
            jconfig = d_rsp['jconfig_raw'][0]
            d_rsp = { 'status_code':200, 'jconfig': jconfig}

        return d_rsp
    

    def set_config(self, unit_id=None, d_config=None):
        """
        """
        self.logger.debug("")      

        # El d_config como viene del request, lo debo re-serializar para que la BD no salte.
        # https://stackoverflow.com/questions/26745519/converting-dictionary-to-json
        #
        #self.logger.debug(f"D_CONFIG={d_config}")
        #jd_config = json.dumps(d_config)
        #self.logger.debug(f"JD_CONFIG={jd_config}")

        return self.repo.set_config(unit_id, d_config)

