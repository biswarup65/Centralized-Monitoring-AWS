import multiprocessing
import time
import os

def cpu_burn(load_percentage):
    """
    Burn CPU based on load percentage.
    Example: 60% load = work 0.6s, sleep 0.4s per second
    """
    work_time = load_percentage / 100
    sleep_time = 1 - work_time

    while True:
        start = time.time()
        # Busy work
        while time.time() - start < work_time:
            pass
        time.sleep(sleep_time)


if __name__ == "__main__":
    cpu_cores = os.cpu_count()
    target_cpu = 60  # Target CPU usage percentage

    # Number of processes to start
    processes_to_run = max(1, int(cpu_cores * (target_cpu / 100)))

    print(f"CPU cores available: {cpu_cores}")
    print(f"Target CPU utilization: {target_cpu}%")
    print(f"Starting {processes_to_run} CPU stress processes")

    processes = []

    for _ in range(processes_to_run):
        p = multiprocessing.Process(target=cpu_burn, args=(target_cpu,))
        p.start()
        processes.append(p)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping CPU spike...")
        for p in processes:
            p.terminate()
