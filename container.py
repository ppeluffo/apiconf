#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

from dependency_injector import containers, providers
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from servicios.pingservice import PingService
from servicios.unidadesservice import UnidadesService
from servicios.configservice import ConfigService
from servicios.uid2idservice import Uid2idService

from repositorios.repopgsql import RepoPgsql

from datasources.pgsql.bdapi import ApiBdPgsql

from utilidades.login_config import configure_logger

from config import settings

class Container(containers.DeclarativeContainer):
    
    wiring_config = containers.WiringConfiguration(
        modules=["resources.pingresource",
                 "resources.helpresource",
                 "resources.unidadesresource",
                 "resources.configresource",
                 "resources.uid2idresource"
                 ]
    )
    
    # Logger (singleton compartido)
    logger = providers.Singleton(configure_logger, name="api-redis")

    # Engine y session factory BDLOCAL
    engine_pgsql = providers.Singleton(
        create_engine,
        url=settings.PGSQL_URL, 
        echo=False, 
        isolation_level="AUTOCOMMIT", 
        connect_args={'connect_timeout': 5}
    )

    session_pgsql = providers.Singleton(
        sessionmaker,
        bind = engine_pgsql
    )
    
    # Datasources
    ds_pgsql = providers.Factory( ApiBdPgsql, session_factory = session_pgsql, logger=logger )
    
    # Repositorios
    repo = providers.Factory(RepoPgsql,datasource=ds_pgsql, logger=logger)
    
    # Servicios
    ping_service = providers.Factory(PingService, repositorio=repo, logger=logger)
    unidades_service = providers.Factory(UnidadesService, repositorio=repo, logger=logger)
    config_service = providers.Factory(ConfigService, repositorio=repo, logger=logger)
    uid2id_service = providers.Factory(Uid2idService, repositorio=repo, logger=logger)





