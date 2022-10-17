from . import crud, database, models, schemas

from loguru import logger


def setup():
    from .database import Base, engine

    logger.info("Creating the persistent log database...")
    Base.metadata.create_all(bind=engine)
    logger.success("Persistent log database has or had been created")
