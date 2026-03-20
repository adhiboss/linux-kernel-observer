import os
import time
import psutil

def read_interrupts():
    with open("/proc/interrupts") as f:
        return f.readlines()

def read_load():
    with open("/proc/loadavg") as f:
        return f.read().strip()

while True:
    os.system("clear")
    print("==== Linux Kernel Activity Observer ====\n")

    print("System Load:")
    print(read_load(), "\n")

    print("CPU Usage Per Core:")
    for i, val in enumerate(psutil.cpu_percent(percpu=True)):
        print(f"Core {i}: {val}%")

    print("\nTop Interrupt Sources:")
    interrupts = read_interrupts()[1:6]
    for line in interrupts:
        print(line.strip())

    print("\nTop Processes:")
    procs = sorted(
        [p.info for p in psutil.process_iter(['pid','name','cpu_percent'])],
        key=lambda x: x['cpu_percent'],
        reverse=True
    )[:5]

    for p in procs:
        print(f"{p['pid']} {p['name']} CPU:{p['cpu_percent']}%")

    time.sleep(3)
