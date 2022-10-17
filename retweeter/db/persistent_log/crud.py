import datetime
import operator

from sqlalchemy.orm import Session

from retweeter.db.persistent_log import models
from retweeter.db.persistent_log import schemas


def get_recent(*, session: Session, seconds: int):
    logs = (
        session.query(models.TweetLog)
        .filter(
            models.TweetLog.crawled_at
            < datetime.datetime.utcnow() - datetime.timedelta(seconds=seconds)
        )
        .all()
    )
    total = len(logs)
    retweeted = sum(map(operator.attrgetter("retweeted"), logs))
    return dict(total=total, retweeted=retweeted, retweet_canceled=total - retweeted)


def get_twitter_user(*, session: Session, twitter_user: schemas.TwitterUserGet):
    user = None
    if twitter_user.id:
        user = session.get(models.TwitterUser, twitter_user.id)
    elif twitter_user.name:
        user = (
            session.query(models.TwitterUser)
            .filter_by(name=twitter_user.name)
            .one_or_none()
        )
    return user


def update_twitter_user(*, session: Session, twitter_user: schemas.TwitterUserUpdate):
    user = get_twitter_user(
        session=session,
        twitter_user=schemas.TwitterUserGet(id=twitter_user.id, name=twitter_user.name),
    )
    if not user:
        user = models.TwitterUser()
    user.id = twitter_user.id
    user.name = twitter_user.name
    user.followers_count = twitter_user.followers_count
    user.friends_count = twitter_user.friends_count
    user.statuses_count = twitter_user.statuses_count
    user.location = twitter_user.location
    session.add(user)
    session.commit()


def create_tweet_log(*, session: Session, tweet_log: schemas.TweetLogCreate):
    update_twitter_user(session=session, twitter_user=tweet_log.user)
    persistent_tweet_log = models.TweetLog(
        tweet_id=tweet_log.tweet_id,
        text=tweet_log.text,
        keyword=tweet_log.keyword,
        location=tweet_log.location,
        target=bool(tweet_log.target),
        retweeted=tweet_log.retweeted,
        user_id=tweet_log.user.id,
    )
    session.add(persistent_tweet_log)
    session.commit()
