import threading
import time
from queue import Queue, Full

MAX_ACTIVE = 2
MAX_QUEUE = 3

semaphore = threading.Semaphore(MAX_ACTIVE)
queue = Queue(maxsize=MAX_QUEUE)


def process_request(request_id):
    with semaphore:
        print(f"{request_id} started to work")
        time.sleep(2)
        print(f"{request_id} finished")


def worker_loop():
    while True:
        request_id = queue.get()

        if request_id is None:
            break

        process_request(request_id)
        queue.task_done()


workers = []

for _ in range(MAX_ACTIVE):
    t = threading.Thread(target=worker_loop)
    t.start()
    workers.append(t)


def submit_request(request_id):
    try:
        queue.put_nowait(request_id)
        print(f"{request_id} sent to the queue")
    except Full:
        print(f"{request_id} Denied - system is full")


for i in range(10):
    submit_request(f"R{i+1}")

queue.join()

for _ in workers:
    queue.put(None)

for t in workers:
    t.join()