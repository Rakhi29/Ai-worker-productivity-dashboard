
from sqlalchemy.orm import Session
from models import Worker, Workstation, Event
from datetime import datetime, timedelta
import random

def seed_data(db: Session):

    db.query(Event).delete()
    db.query(Worker).delete()
    db.query(Workstation).delete()
    db.commit()

    workers = [Worker(worker_id=f"W{i}", name=f"Worker {i}") for i in range(1,7)]
    stations = [Workstation(station_id=f"S{i}", name=f"Station {i}") for i in range(1,7)]

    db.add_all(workers + stations)
    db.commit()

    base_time = datetime.utcnow()

    for i in range(120):
        event = Event(
            timestamp=base_time + timedelta(minutes=i*5),
            worker_id=f"W{random.randint(1,6)}",
            workstation_id=f"S{random.randint(1,6)}",
            event_type=random.choice(["working","idle","product_count"]),
            confidence=0.9,
            count=random.randint(1,5)
        )
        db.add(event)

    db.commit()
