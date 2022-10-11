# This is to make queries to PostgreSQL via SQL Alchemy
from retweeter.db.persistent_log.database import SessionLocal

# That's for connecting to the PostgreSQL
session = SessionLocal()


def get_recent_seconds_stats(session, seconds: int):
    logs = (
        session.query(ClassificationLog)
        .filter(ClassificationLog.created_at < datetime.datetime.utcnow() - seconds)
        .all()
    )
    total = len(logs)
    retweeted = sum(map(operator.attrgetter("retweeted"), logs))
    retweet_canceled = total - retweeted
    return dict(total=total, retweeted=retweeted, retweet_canceled=retweet_canceled)
