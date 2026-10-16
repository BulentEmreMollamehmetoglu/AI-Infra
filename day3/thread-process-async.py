import threading
import time
import asyncio
from multiprocessing import Process as MPProcess


# -------------------------
# THREAD DEMO
# -------------------------

class ThreadDemo:
    def work(self, name):
        print(name, "started")
        time.sleep(2)
        print(name, "finished")

    def run(self):
        t1 = threading.Thread(target=self.work, args=("T1",))
        t2 = threading.Thread(target=self.work, args=("T2",))

        t1.start()
        t2.start()

        t1.join()
        t2.join()


# -------------------------
# PROCESS DEMO
# -------------------------

def process_work(name):
    print(name, "started")
    time.sleep(2)
    print(name, "finished")


def run_process_demo():
    p1 = MPProcess(target=process_work, args=("P1",))
    p2 = MPProcess(target=process_work, args=("P2",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


# -------------------------
# ASYNC DEMO
# -------------------------

async def async_work(name):
    print(name, "started")
    await asyncio.sleep(2)
    print(name, "finished")


async def run_async_demo():
    await asyncio.gather(
        async_work("A"),
        async_work("B"),
        async_work("C"),
    )


# -------------------------
# MAIN
# -------------------------

if __name__ == "__main__":

    print("\n--- THREADS ---")
    ThreadDemo().run()

    print("\n--- PROCESSES ---")
    run_process_demo()

    print("\n--- ASYNC TASKS ---")
    asyncio.run(run_async_demo())