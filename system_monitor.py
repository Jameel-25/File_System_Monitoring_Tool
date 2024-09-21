import psutil
import time

def monitor_system():
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        print(f"CPU Usage: {cpu_usage}%, Memory Usage: {memory_info.percent}%")
        time.sleep(5)

def log_system_stats(log_file):
    with open(log_file, 'a') as f:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory_info = psutil.virtual_memory()
            f.write(f"CPU Usage: {cpu_usage}%, Memory Usage: {memory_info.percent}%\n")
            f.flush()
            time.sleep(10)
