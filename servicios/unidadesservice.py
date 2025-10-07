#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

class UnidadesService:
    """
    """
    def __init__(self, repositorio, logger):
        self.repo = repositorio
        self.logger = logger

    def get_all_unidades(self):
        """
        """
        self.logger.debug("")
        
        d_rsp = self.repo.get_only_plc()
        l_plcs = []        
        if d_rsp.get('status_code',0) == 200:
            plcs_raw = d_rsp['plcs_raw']
            l_plcs = [ element.unit_id for element in plcs_raw]
        else:
            return d_rsp

        d_rsp = self.repo.get_only_dlgs()
        l_dlgs = []        
        if d_rsp.get('status_code',0) == 200:
            dlgs_raw = d_rsp['dlgs_raw']
            l_dlgs = [ element.unit_id for element in dlgs_raw]
            d_rsp = { 'status_code':200, 
                     'nro_plcs': len(l_plcs), 'l_plcs': l_plcs,
                     'nro_dlgs': len(l_dlgs), 'l_dlgs': l_dlgs
                     }

        return d_rsp
    
        """
        l_unidades = []        
        if d_rsp.get('status_code',0) == 200:
            unidades_raw = d_rsp['unidades_raw']
            l_unidades = [ element.unit_id for element in unidades_raw]
            d_rsp = { 'status_code':200, 'nro_unidades': len(l_unidades), 'l_unidades': l_unidades}

        return d_rsp
        """
