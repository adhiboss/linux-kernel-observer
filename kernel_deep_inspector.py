import os
import time
import psutil

def read_file(path):
    try:
        with open(path) as f:
            return f.read().strip()
    except:
        return "N/A"

while True:
    os.system("clear")

    print("========== Linux Kernel Deep Inspector ==========\n")

    print("Kernel Version:")
    print(read_file("/proc/version"), "\n")

    print("System Uptime:")
    print(read_file("/proc/uptime"), "\n")

    print("Load Average:")
    print(read_file("/proc/loadavg"), "\n")

    print("CPU Usage Per Core:")
    for i, cpu in enumerate(psutil.cpu_percent(percpu=True)):
        print(f"Core {i}: {cpu}%")

    print("\nMemory Info:")
    mem = psutil.virtual_memory()
    print(f"Total: {mem.total//(1024**3)} GB")
    print(f"Used : {mem.used//(1024**3)} GB")
    print(f"Usage: {mem.percent}%")

    print("\nTop Processes:")
    processes = sorted(
        [p.info for p in psutil.process_iter(['pid','name','cpu_percent'])],
        key=lambda x: x['cpu_percent'],
        reverse=True
    )[:5]

    for p in processes:
        print(f"{p['pid']} | {p['name']} | CPU {p['cpu_percent']}%")

    print("\nWatching kernel activity... refresh in 3s")
    time.sleep(3)
