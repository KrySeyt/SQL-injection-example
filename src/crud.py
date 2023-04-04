from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from src.schema import ClientIn


def unsafe_create_client(db: Session, client: ClientIn):
    stmt = text(f"INSERT INTO clients_table(name) VALUES ('{client.name}');")
    result = db.execute(stmt)
    db.commit()
    return result


def safe_create_client(db: Session, client: ClientIn):
    stmt = text("INSERT INTO clients_table(name) VALUES (:client_name);")
    result = db.execute(stmt, {"client_name": client.name})
    db.commit()
    return result
