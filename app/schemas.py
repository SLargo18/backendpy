from pydantic import BaseModel
from datetime import datetime

class EventBase(BaseModel):
    name: str
    date_time: datetime
    location: str
    type: str

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int

    class Config:
        orm_mode = True