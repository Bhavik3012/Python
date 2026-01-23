import time

wait_time = 1
max_retries = 5
attempt = 0

while attempt < max_retries:
    print("Attempt", attempt + 1, "- waiting time", wait_time, "seconds")
    time.sleep(wait_time)
    wait_time *= 2
    attempt += 1
