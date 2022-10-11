# Import engine, which is the connection to Redis database
from retweeter.db.database import engine


def get_analytics_data():

    return {
        "last_ack": engine.get("last_ack"),
        "ack_timeout": engine.get("ack_timeout"),
        "classified": engine.hgetall("classified"),
        "api_limits": engine.hgetall("api_limits"),
        "statistics": engine.hgetall("statistics"),
    }
