import time
import json
import psutil

LOG_FILE = "kernel_timetravel_log.json"

def snapshot():
    data = {
        "timestamp": time.time(),
        "cpu_percent": psutil.cpu_percent(percpu=True),
        "memory": psutil.virtual_memory()._asdict(),
        "processes": [
            p.info for p in psutil.process_iter(['pid','name','cpu_percent'])
        ]
    }
    return data

history = []

try:
    while True:
        snap = snapshot()
        history.append(snap)

        with open(LOG_FILE,"w") as f:
            json.dump(history, f, indent=2)

        print("Snapshot recorded:", len(history))
        time.sleep(5)

except KeyboardInterrupt:
    print("Recording stopped")
