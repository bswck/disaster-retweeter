from __future__ import annotations

from fastapi import FastAPI

from retweeter_web.app.routers import analytics, logs

# from routers import analytics, logs

app = FastAPI()
app.include_router(analytics.router, prefix="/analytics")
app.include_router(logs.router, prefix="/logs")
