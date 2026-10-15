import threading
import time

lock_a = threading.Lock()
lock_b = threading.Lock()

def worker_1():
    print("T1: lock_a is waiting")
    with lock_a:
        print("T1: took the lock_a")
        time.sleep(0.5)

        print("T1: lock_b is waiting")
        with lock_b:
            print("T1: took the both locks")

def worker_2():
    print("T2: lock_a is waiting")
    with lock_a:
        print("T2: took the lock_a")
        time.sleep(0.5)

        print("T2: lock_b is waiting")
        with lock_b:
            print("T2: took the both locks")

t1 = threading.Thread(target=worker_1)
t2 = threading.Thread(target=worker_2)

t1.start()
t2.start()

t1.join()
t2.join()

print("Done")