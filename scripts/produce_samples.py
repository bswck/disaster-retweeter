import contextlib
import random

from loguru import logger

from scripts.test_stage import test_stage  # noqa: F401

from retweeter.db import persistent_log
from retweeter.db.persistent_log.database import get_session
from retweeter.db.persistent_log.schemas import TweetLogCreate, TwitterUserUpdate


def generate_persistent_log_samples():
    persistent_log.setup()
    return (
        # /original/test.csv#L1984
        TweetLogCreate(
            tweet_id=random.randint(0, 10000),
            keyword="crashed",
            location="Pakistan",
            text="Maj Muzzamil Pilot Offr of MI - 17 crashed near Mansehra today. http://t.co/kL4R1ccWct",
            target=1,
            retweeted=True,
            user=TwitterUserUpdate(
                id=1263391244451961467,
                name='SomeFakeTwitterUser',
                followers_count=8557,
                friends_count=492,
                statuses_count=286,
                location='GBR'
            )
        ),
        # /original/test.csv#L40
        TweetLogCreate(
            tweet_id=random.randint(0, 10000),
            keyword='cliff%20fall',
            location='USA',
            text='If u faved that I hope you fall off a cliff ??',
            target=0,
            retweeted=False,
            user=TwitterUserUpdate(
                id=1577769255798933172,
                name='Foo',
                followers_count=2805,
                friends_count=910,
                statuses_count=120,
                location='USA'
            )
        ),
        # /original/test.csv#L119
        TweetLogCreate(
            tweet_id=random.randint(0, 10000),
            keyword='aftershock',
            location=None,
            text="#GrowingUpSpoiled going clay pigeon shooting and crying because of the 'aftershock'",
            target=0,
            retweeted=False,
            user=TwitterUserUpdate(
                id=1191220455073153820,
                name='Bar',
                followers_count=8976,
                friends_count=989,
                statuses_count=674,
                location='POL'
            )
        ),
        # /original/test.csv#L2269
        TweetLogCreate(
            tweet_id=random.randint(0, 10000),
            keyword='danger',
            location=None,
            text='SO THIRSTY YALL IN DANGER OF DEHYDRATION',
            target=1,
            retweeted=True,
            user=TwitterUserUpdate(
                id=1403599659453070551,
                name='Josh',
                followers_count=9705,
                friends_count=986,
                statuses_count=353,
                location='ESP'
            )
        ),
        # /original/test.csv#L2410
        TweetLogCreate(
            tweet_id=random.randint(0, 10000),
            keyword='debris',
            location=None,
            text='RÌ©union Debris Is Almost Surely From Flight 370 Officials Say - New York Times http://t.co/gyQLAOz3l2',
            target=1,
            retweeted=True,
            user=TwitterUserUpdate(
                id=1003599659453070651,
                name='Josh',
                followers_count=9708,
                friends_count=987,
                statuses_count=368,
                location='ESP'
            )
        )
    )


def feed_persistent_log(samples=None):
    if samples is None:
        samples = generate_persistent_log_samples()
    crud = persistent_log.crud
    session_maker = contextlib.contextmanager(get_session)
    for sample_tweet_log in samples:
        with session_maker() as session:
            crud.create_tweet_log(
                session=session,
                tweet_log=sample_tweet_log
            )
            logger.success(f"Added tweet log: {sample_tweet_log}")


if __name__ == '__main__':
    feed_persistent_log()
