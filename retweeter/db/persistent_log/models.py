from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy import text
from sqlalchemy.orm import relationship
from retweeter.db.persistent_log.database import Base


class TwitterUser(Base):
    __tablename__ = "twitter_users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    url = Column(String)
    followers_count = Column(Integer)
    friends_count = Column(Integer)
    statuses_count = Column(Integer)
    location = Column(String)


class ClassificationLog(Base):
    __tablename__ = "classification_logs"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, server_default=text("TIMEZONE('UTC', NOW())"))
    text = Column(String)
    url = Column(String)
    keyword = Column(String)
    location = Column(String)
    target = Column(Boolean)
    # this is being queried
    retweeted = Column(Boolean)
    user_id = Column(Integer, ForeignKey("twitter_users.id"))
    user = relationship("TwitterUser", back_populates="classification_logs")
