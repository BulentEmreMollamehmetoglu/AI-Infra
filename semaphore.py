# lock -> allows 1 process to enter
# semaphore -> allows N process to enter

import threading
import time

semaphore = threading.Semaphore(2)

def worker(name):
    print(name, "waiting")

    with semaphore:
        print(name, "inside")
        time.sleep(2)
        print(name, "leaving")


threads = []

for i in range(5):
    t = threading.Thread(target=worker, args=(f"T{i+1}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()