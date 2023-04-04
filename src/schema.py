from pydantic import BaseModel


class Base(BaseModel):
    pass


class ClientBase(Base):
    name: str


class ClientIn(ClientBase):
    pass
