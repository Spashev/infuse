import os
import contextlib
from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from apscheduler.schedulers.background import BackgroundScheduler

from app import api
from app.core import settings
from app.database.models import BaseModel
from app.database import engine_dev, engine_prod, get_dev_db, get_prod_db
from app.core.exceptions import handle_exceptions
from app.sync.database_sync import sync_data

load_dotenv()
os.makedirs(settings.UPLOAD_DIRECTORY, exist_ok=True)


def sync_databases():
    dev_session = next(get_dev_db())
    prod_session = next(get_prod_db())
    try:
        sync_data(dev_session, prod_session)
    finally:
        dev_session.close()
        prod_session.close()


scheduler = BackgroundScheduler()
scheduler.add_job(sync_databases, 'interval', minutes=1)


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    BaseModel.metadata.create_all(bind=engine_dev)
    BaseModel.metadata.create_all(bind=engine_prod)
    scheduler.start()
    handle_exceptions(app=app)
    yield
    scheduler.shutdown()


def initialize():
    app = FastAPI(
        title="Infuse",
        debug=settings.DEBUG,
        version="0.0.1",
        docs_url="/swagger",
        redoc_url="/redoc",
        lifespan=lifespan
    )
    app.mount("/static", StaticFiles(directory=settings.UPLOAD_DIRECTORY), name="static")
    app.include_router(api.router)

    return app


app = initialize()
