from __future__ import annotations

import pydantic


class BaseTwitterUser(pydantic.BaseModel):
    id: int


class TwitterUserGet(BaseTwitterUser):
    id: int | None
    name: str


class TwitterUserUpdate(BaseTwitterUser):
    name: str
    followers_count: int
    friends_count: int
    statuses_count: int
    location: str


class BaseTweetLog(pydantic.BaseModel):
    tweet_id: int


class TweetLogCreate(BaseTweetLog):
    text: str
    keyword: str
    location: str | None
    retweeted: bool
    user: TwitterUserUpdate
    target: int  # 0 or 1
