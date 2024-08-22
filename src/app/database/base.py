from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import DBAPIError

from app.core import settings

engine_dev = create_engine(url=settings.get_dev_url, echo=settings.ECHO)
session_maker_dev = sessionmaker(autocommit=False, autoflush=False, bind=engine_dev)

engine_prod = create_engine(url=settings.get_prod_url, echo=settings.ECHO)
session_maker_prod = sessionmaker(autocommit=False, autoflush=False, bind=engine_prod)


def get_dev_db():
    session_dev = session_maker_dev()
    try:
        yield session_dev
    except DBAPIError:
        session_dev.rollback()
    finally:
        session_dev.close()


def get_prod_db():
    session_prod = session_maker_prod()
    try:
        yield session_prod
    except DBAPIError:
        session_prod.rollback()
    finally:
        session_prod.close()
