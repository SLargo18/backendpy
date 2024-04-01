from sqlalchemy import Column, Integer, String, DateTime
from app.config import Base
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    date_time = Column(DateTime, nullable=False)
    location = Column(String, nullable=False)
    type = Column(String, nullable=False)

    def to_dict(self):
        return {
            "id":self.id,
            "name": self.name,
            "dateTime": self.date_time,
            "location": self.location,
            "type": self.type
        }

