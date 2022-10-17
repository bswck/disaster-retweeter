from __future__ import annotations

from fastapi import APIRouter
from sqlalchemy.orm import Session

from retweeter.db import analytics
from retweeter.db import persistent_log

router = APIRouter()


@router.get("/")
async def get_analytics():
    return analytics.crud.get_analytics()


@router.get("/recent/{seconds}")
async def get_recent(
    seconds: int,
    session: Session = persistent_log.database.session
):
    return persistent_log.crud.get_recent(seconds=seconds, session=session)


def create_router():
    return router
