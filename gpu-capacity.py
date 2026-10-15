import threading
import time

gpu_slots = threading.Semaphore(2)


def inference(request_id):
    print(request_id, "waiting for GPU")

    with gpu_slots:
        print(request_id, "using GPU")
        time.sleep(2)
        print(request_id, "finished GPU work")


threads = []

for i in range(10):
    t = threading.Thread(
        target=inference,
        args=(f"R{i+1}",)
    )

    threads.append(t)
    t.start()


for t in threads:
    t.join()