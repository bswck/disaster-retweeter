import os
import traceback

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


USERNAME = os.getenv("PERSISTENT_LOG_DB_USERNAME")
NAME = os.getenv("PERSISTENT_LOG_DB_NAME", USERNAME)
PASSWORD = os.getenv("PERSISTENT_LOG_DB_PASSWORD")
HOST = os.getenv("PERSISTENT_LOG_DB_HOST", "localhost")
PORT = os.getenv("PERSISTENT_LOG_DB_PORT", "5432")

URL = f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{NAME}"

engine = create_engine(URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


def get_session(session_factory=None):
    if session_factory is None:
        session_factory = SessionLocal

    wrapped_session = session_factory()

    try:
        yield wrapped_session
    except SQLAlchemyError:
        traceback.print_exc()

    else:
        try:
            wrapped_session.commit()
        except SQLAlchemyError:
            wrapped_session.rollback()
            traceback.print_exc()

    finally:
        wrapped_session.close()


session = Depends(get_session)
