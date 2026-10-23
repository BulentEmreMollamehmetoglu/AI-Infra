
import asyncio

counter = 0
lock = asyncio.Lock()


async def increment(name):
    global counter

    for _ in range(3):
    
        current = counter
        print(name, "read:", current)

        await asyncio.sleep(0.2)

        counter = current + 1
        print(name, "wrote:", counter)


async def main():
    await asyncio.gather(
        increment("A"),
        increment("B")
    )

    print("Final counter:", counter)


asyncio.run(main())
