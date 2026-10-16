import time


def fetch(name):
    print(name, "started")
    time.sleep(2)
    print(name, "finished")


started = time.time()

fetch("A")
fetch("B")
fetch("C")

print("Total:", time.time() - started)




