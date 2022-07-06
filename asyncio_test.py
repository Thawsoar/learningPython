import time
import asyncio

import aiohttp


def test(number):
    start_time = time.time()

    async def get(url):
        session = aiohttp.ClientSession()
        response = await session.get(url)
        await response.text()
        await session.close()
        return response

    async def request():
        url = "https://www.baidu.com"
        await get(url)

    tasks = [
        asyncio.ensure_future(request()) for _ in range(number)
    ]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))

    end_time = time.time()
    print("Number:", number, "Cost time", end_time - start_time)
    asyncio.gather()

if __name__ == '__main__':
    for num in [1, 3, 5, 10, 15, 30, 50, 75, 100, 200, 400]:
        test(num)
