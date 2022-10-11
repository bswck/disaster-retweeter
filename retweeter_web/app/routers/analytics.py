from __future__ import annotations

from fastapi import APIRouter, Depends

from retweeter.db.analytics.crud import get_analytics_data

# Import function to query PostgreSQL
from retweeter.db.persistent_log.crud import get_recent_seconds_stats

router = APIRouter()


@router.get("/")
async def obtain_analytics_data():
    return get_analytics_data()


@router.get("/recent/{seconds}")
async def obtain_number_of_tweets_classified_in_last_n_seconds(
    seconds, session=Depends(get_session)
):
    return get_recent_seconds_stats(session)
