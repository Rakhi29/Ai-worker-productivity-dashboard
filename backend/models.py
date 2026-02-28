
from sqlalchemy import Column, String, Float, Integer, DateTime, ForeignKey
from database import Base
import uuid

class Worker(Base):
    __tablename__ = "workers"
    worker_id = Column(String, primary_key=True, index=True)
    name = Column(String)

class Workstation(Base):
    __tablename__ = "workstations"
    station_id = Column(String, primary_key=True, index=True)
    name = Column(String)

class Event(Base):
    __tablename__ = "events"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    timestamp = Column(DateTime)
    worker_id = Column(String, ForeignKey("workers.worker_id"))
    workstation_id = Column(String, ForeignKey("workstations.station_id"))
    event_type = Column(String)
    confidence = Column(Float)
    count = Column(Integer, default=0)
