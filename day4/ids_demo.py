
import os
import threading
import asyncio
from multiprocessing import Process


def show_ids(name):
    print(
        f"{name}: "
        f"PID={os.getpid()}, "
        f"Thread ID={threading.get_ident()}",
        flush=True
    )


def thread_work(name):
    show_ids(name)


def process_work(name):
    show_ids(name)


async def async_work(name):
    show_ids(name)
    await asyncio.sleep(0.5)


async def async_demo():
    await asyncio.gather(
        async_work("Async A"),
        async_work("Async B"),
        async_work("Async C")
    )


if __name__ == "__main__":

    print("\n--- THREADS ---")
    show_ids("Main")

    t1 = threading.Thread(target=thread_work, args=("T1",))
    t2 = threading.Thread(target=thread_work, args=("T2",))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("\n--- PROCESSES ---")

    p1 = Process(target=process_work, args=("P1",))
    p2 = Process(target=process_work, args=("P2",))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print("\n--- ASYNC ---")
    asyncio.run(async_demo())
