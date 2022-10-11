from __future__ import annotations

import traceback

from fastapi import APIRouter
from sqlalchemy.exc import SQLAlchemyError

from retweeter.db.persistent_log import database, models


models.Base.metadata.create_all(bind=database.engine)


def get_session(session_factory=database.SessionLocal):
    session = session_factory()

    try:
        yield session
    except SQLAlchemyError:
        traceback.print_exc()

    else:
        try:
            session.commit()
        except SQLAlchemyError:
            session.rollback()
            traceback.print_exc()

    finally:
        session.close()


router = APIRouter()
