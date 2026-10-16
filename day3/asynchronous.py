import asyncio
import time


async def fetch(name):
    print(name, "started")
    await asyncio.sleep(2)
    print(name, "finished")


async def main():
    started = time.time()

    await asyncio.gather(
        fetch("A"),
        fetch("B"),
        fetch("C"),
    )

    print("Total:", time.time() - started)


asyncio.run(main())

