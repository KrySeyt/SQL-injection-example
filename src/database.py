import os
from functools import lru_cache

from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session


def get_postgres_url() -> str:
    postgres_url = os.getenv("POSTGRESQL_URL")

    database_url_data = postgres_url[postgres_url.find(':'):]
    sqlalchemy_database_url = f"postgresql+psycopg2{database_url_data}"

    return sqlalchemy_database_url


@lru_cache(maxsize=1)
def get_engine() -> Engine:
    db_url = get_postgres_url()
    engine = create_engine(db_url, echo=True, future=True)
    return engine


def get_session() -> Session:
    engine = get_engine()
    return sessionmaker(bind=engine)()
