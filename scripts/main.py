from __future__ import annotations

from fastapi import FastAPI

try:
    import dotenv
except ImportError:
    dotenv = None  # pragma: nocover
else:
    dotenv.load_dotenv()

from retweeter_web.app.routers import analytics
from retweeter_web.app.routers import logs

if __debug__:
    from test_stage import setup_test_stage
    setup_test_stage()

ROUTERS = {"/logs": logs}


def create_app(routers):
    application = FastAPI()

    for prefix, router_module in routers.items():
        application.include_router(router_module.create_router(), prefix=prefix)

    return application


app = create_app(routers=ROUTERS)
