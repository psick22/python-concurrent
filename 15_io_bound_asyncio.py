import asyncio
import aiohttp
import time


async def request_url(url, session):
    # print(session)
    # print(session.headers)
    async with session.get(url) as response:
        print(f'Read Contents {response.content_length} from {url}')


async def request_all_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.ensure_future(request_url(url, session))
            tasks.append(task)

        # await asyncio.gather(*tasks, return_exceptions=True)
        await asyncio.wait(tasks)

def main():
    # 테스트 URL
    URLS = ["http://www.jython.org",
            "http://www.youtube.com",
            "http://realpython.com",
            "http://olympus.realpython.org/dice", ] * 15

    start_time = time.time()

    asyncio.run(request_all_urls(URLS))

    duration = time.time() - start_time
    print()
    print(f"Downloaded {len(URLS)} urls in {duration} seconds")


if __name__ == "__main__":
    main()
