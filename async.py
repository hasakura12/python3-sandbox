from timeit import default_timer
import requests
import aiohttp
import asyncio # for python > 3.7

def load_synchronous(delay: int) -> str:
    print(f"Starting {delay} timer...")
    text = requests.get(f"https://httpbin.org/delay/{delay}").text
    print(f"Ending {delay} timer...")
    return text

# async making python runtime become aware there will be pause and also callback
async def load_async(session, delay: int) -> str:
    print(f"Starting {delay} timer...")
    async with session.get(f"https://httpbin.org/delay/{delay}") as response:
        # blocking call
        text = await response.text()
        print(f"Ending {delay} timer...")
        return text


# print(f"Synchronous call response is {load_synchronous(delay=2)}")

async def main():
    start_time = default_timer()

    # creating single session
    # ref: https://www.youtube.com/watch?v=1UPpOheLFrs&list=PLlrxD0HtieHiXd-nEby-TMCoUNwhbLUnj&index=19
    # session aiohttp.ClientSession() > wrap response session.get() call inside asyncio.create_task() 
    async with aiohttp.ClientSession() as session:
        # create a process
        task = asyncio.create_task(load_async(session, 2))

        await asyncio.sleep(1)
        print("Doing other work...")

        # not like this: response = load_async(session, 2)
        result = await task
        print(f"Async call response is {result}")

        elapsed_time = default_timer() - start_time
        print(f"Operations took {elapsed_time:.2} sec")


asyncio.run(main())