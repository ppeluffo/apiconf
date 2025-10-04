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
        
        d_rsp = self.repo.get_all_unidades()

        l_unidades = []        
        if d_rsp.get('rsp','ERR') == 'OK':

            unidades_raw = d_rsp['unidades_raw']
            l_unidades = [ element.unit_id for element in unidades_raw]
            d_rsp = { 'rsp':'OK', 'nro_unidades': len(l_unidades), 'l_unidades': l_unidades}

        return d_rsp
    