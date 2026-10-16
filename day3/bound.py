import asyncio
import time


async def heavy_work(name):
    print(name, "started")

    total = 0

    for i in range(30_000_000):
        total += i

    print(name, "finished")

async def io_work(name):
    print(name, "started")

    await asyncio.sleep(2)

    print(name, "finished")

async def main():
    started = time.time()

    await asyncio.gather(
        io_work("A"),
        io_work("B"),
        io_work("C"),
    )

    print("Total:", time.time() - started)


asyncio.run(main())