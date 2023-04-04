from sqlalchemy.orm import Session

from src.schema import ClientIn
from src import crud


def unsafe_create_client(db: Session, client: ClientIn) -> str:
    result = crud.unsafe_create_client(db, client)
    print(f"Result: {result}")
    return "Done"


def safe_create_client(db: Session, client: ClientIn) -> str:
    result = crud.safe_create_client(db, client)
    print(f"Result: {result}")
    return "Done"
