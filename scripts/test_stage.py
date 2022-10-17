import os
import runpy
import sys
import time

from loguru import logger

_test_stage = None


def setup_test_stage():
    global _test_stage
    # try to load environment variables from .env file
    try:
        import dotenv
    except ImportError:
        pass
    else:
        dotenv.load_dotenv()

    # monkeypatch production environment variables for testing purposes
    # 0% risk: production environment variables are overridden
    os.environ.update(
        PERSISTENT_LOG_DB_USERNAME=os.getenv("TEST_PERSISTENT_LOG_DB_USERNAME"),
        PERSISTENT_LOG_DB_PASSWORD=os.getenv("TEST_PERSISTENT_LOG_DB_PASSWORD"),
        PERSISTENT_LOG_DB_HOST=os.getenv("TEST_PERSISTENT_LOG_DB_HOST"),
        PERSISTENT_LOG_DB_PORT=os.getenv("TEST_PERSISTENT_LOG_DB_PORT", "5432"),
        ANALYTICS_DB_USERNAME=os.getenv("TEST_ANALYTICS_DB_USERNAME"),
        ANALYTICS_DB_PASSWORD=os.getenv("TEST_ANALYTICS_DB_PASSWORD"),
        ANALYTICS_DB_HOST=os.getenv("TEST_ANALYTICS_DB_HOST"),
        ANALYTICS_DB_PORT=os.getenv("TEST_ANALYTICS_DB_PORT", "6379"),
    )

    _test_stage = dict(
        started_at=time.perf_counter()
    )

    logger.success("Test stage has been set up successfully")


def __getattr__(name):
    global _test_stage

    if name == "test_stage":
        if not _test_stage:
            setup_test_stage()
        return _test_stage


if __name__ == '__main__':
    if len(sys.argv) == 2:
        setup_test_stage()
        runpy.run_path(sys.argv[1])
