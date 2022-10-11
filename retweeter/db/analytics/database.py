import os

import redis

IS_UNIX = hasattr(os, "uname")
SCHEME = "unix" if IS_UNIX else "redis"

USERNAME = os.getenv("ANALYTICS_DB_USERNAME")
PASSWORD = os.getenv("ANALYTICS_DB_PASSWORD")
HOST = os.getenv("ANALYTICS_DB_HOST", "localhost")
PORT = os.getenv("ANALYTICS_DB_PORT", "6379")
URL = f"{SCHEME}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/0"

# Redis instance
engine = redis.Redis.from_url(URL)
# Import this to analytics.py and refer this way: "engine.get()"
