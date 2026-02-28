
from collections import defaultdict

def compute_metrics(events):
    worker_metrics = defaultdict(lambda: {
        "active_time_hours": 0,
        "idle_time_hours": 0,
        "units_produced": 0
    })

    events = sorted(events, key=lambda x: x.timestamp)

    for i in range(len(events) - 1):
        curr = events[i]
        nxt = events[i+1]
        delta = (nxt.timestamp - curr.timestamp).total_seconds() / 3600

        if curr.event_type == "working":
            worker_metrics[curr.worker_id]["active_time_hours"] += delta
        elif curr.event_type == "idle":
            worker_metrics[curr.worker_id]["idle_time_hours"] += delta
        elif curr.event_type == "product_count":
            worker_metrics[curr.worker_id]["units_produced"] += curr.count

    for w in worker_metrics:
        active = worker_metrics[w]["active_time_hours"]
        idle = worker_metrics[w]["idle_time_hours"]
        total = active + idle
        worker_metrics[w]["utilization_percent"] = (active / total * 100) if total > 0 else 0
        worker_metrics[w]["units_per_hour"] = (worker_metrics[w]["units_produced"] / active) if active > 0 else 0

    return worker_metrics
