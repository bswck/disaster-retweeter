import os
import runpy
import sys
import time

from loguru import logger


def setup_test_stage():
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
        PERSISTENT_LOG_DB_USERNAME=os.getenv("TEST_PERSISTENT_LOG_DB_USERNAME") or "",
        PERSISTENT_LOG_DB_PASSWORD=os.getenv("TEST_PERSISTENT_LOG_DB_PASSWORD") or "",
        PERSISTENT_LOG_DB_HOST=os.getenv("TEST_PERSISTENT_LOG_DB_HOST") or "",
        PERSISTENT_LOG_DB_PORT=os.getenv("TEST_PERSISTENT_LOG_DB_PORT", "5432"),
        ANALYTICS_DB_USERNAME=os.getenv("TEST_ANALYTICS_DB_USERNAME") or "",
        ANALYTICS_DB_PASSWORD=os.getenv("TEST_ANALYTICS_DB_PASSWORD") or "",
        ANALYTICS_DB_HOST=os.getenv("TEST_ANALYTICS_DB_HOST") or "",
        ANALYTICS_DB_PORT=os.getenv("TEST_ANALYTICS_DB_PORT", "6379"),
    )

    logger.success("Test stage has been set up successfully")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        setup_test_stage()
        runpy.run_path(sys.argv[1])
