import threading
import time

counter = 0

lock = threading.Lock()
def increment():
    global counter

    for _ in range(1000):
        with lock:
            current = counter
            time.sleep(0.0001)
            counter = current + 1

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()


print("Expected:", 2000)
print("Actual:", counter)