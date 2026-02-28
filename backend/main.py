
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, Base, SessionLocal
import models
from schemas import EventCreate
from seed import seed_data
from metrics import compute_metrics

app = FastAPI(title="AI Worker Productivity Dashboard")

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/seed")
def seed(db: Session = Depends(get_db)):
    seed_data(db)
    return {"message": "Database seeded successfully"}

@app.post("/events")
def ingest_event(event: EventCreate, db: Session = Depends(get_db)):
    db_event = models.Event(**event.dict())
    db.add(db_event)
    db.commit()
    return {"message": "Event stored successfully"}

@app.get("/metrics")
def get_metrics(db: Session = Depends(get_db)):
    events = db.query(models.Event).all()
    return compute_metrics(events)
