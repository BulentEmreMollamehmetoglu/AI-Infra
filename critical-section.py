import threading
import time

counter = 0
lock = threading.Lock()

def worker(name):
    global counter

    for _ in range(3):
        print(name, "normal work")
        time.sleep(0.2)

        with lock:
            print(name, "entered critical section")
            current = counter
            time.sleep(0.5)
            counter = current + 1
            print(name, "leaving critical section:", counter)

t1 = threading.Thread(target=worker, args=("T1",))
t2 = threading.Thread(target=worker, args=("T2",))

t1.start()
t2.start()

t1.join()
t2.join()

print("Final:", counter)