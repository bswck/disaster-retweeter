from sqlalchemy import Column, ForeignKey, BigInteger, BIGINT, Integer, String, DateTime, Boolean
from sqlalchemy import text
from sqlalchemy.orm import relationship

from retweeter.db.persistent_log.database import Base


class TwitterUser(Base):
    __tablename__ = "twitter_users"

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String)
    followers_count = Column(Integer)
    friends_count = Column(Integer)
    statuses_count = Column(Integer)
    location = Column(String)
    tweet_logs = relationship("TweetLog", back_populates="user")


class TweetLog(Base):
    __tablename__ = "tweet_logs"

    tweet_id = Column(BigInteger, primary_key=True, index=True)
    crawled_at = Column(DateTime, server_default=text("TIMEZONE('UTC', NOW())"))
    text = Column(String)
    keyword = Column(String)
    location = Column(String)
    target = Column(Boolean)
    retweeted = Column(Boolean)
    user_id = Column(BigInteger, ForeignKey("twitter_users.id"))
    user = relationship("TwitterUser", back_populates="tweet_logs")
