from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends

from src.database import get_session
from src.schema import ClientIn
from src import service


app = FastAPI()


def get_db_session_mock() -> None:
    pass


@app.post("/client_unsafe")
def unsafe_create_client(client: ClientIn, db: Session = Depends(get_db_session_mock)):
    return service.unsafe_create_client(db, client)


@app.post("/client_safe")
def safe_create_client(client: ClientIn, db: Session = Depends(get_db_session_mock)):
    return service.safe_create_client(db, client)


app.dependency_overrides[get_db_session_mock] = get_session
