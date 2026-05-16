import psutil
from datetime import datetime

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80


def log_alert(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    alert = f"[{timestamp}] ALERT: {message}"
    print(alert)

    with open("system_health.log", "a") as file:
        file.write(alert + "\n")


def main():
    print("=== System Health Monitoring ===")

    cpu = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu}%")
    if cpu > CPU_THRESHOLD:
        log_alert(f"CPU usage exceeded {CPU_THRESHOLD}%")

    memory = psutil.virtual_memory()
    print(f"Memory Usage: {memory.percent}%")
    if memory.percent > MEMORY_THRESHOLD:
        log_alert(f"Memory usage exceeded {MEMORY_THRESHOLD}%")

    disk_path = "/" if psutil.WINDOWS is False else "C:\\"
    disk = psutil.disk_usage(disk_path)
    print(f"Disk Usage: {disk.percent}%")
    if disk.percent > DISK_THRESHOLD:
        log_alert(f"Disk usage exceeded {DISK_THRESHOLD}%")

    print(f"Running Processes: {len(psutil.pids())}")


if __name__ == "__main__":
    main()