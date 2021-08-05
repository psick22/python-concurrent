import concurrent.futures
import threading

import requests
import time


# sync - blocking

def request_url(url, session):
    # print(session)
    # print(session.headers)

    with session.get(url) as response:
        print(f'[Read Contents : {len(response.content)}, Status Code : {response.status_code} from {url}]')


def request_all_urls(urls):
    # 멀티쓰레드
    with requests.Session() as session:
        for url in urls:
            request_url(url, session)


def main():
    # 테스트 URL
    URLS = ["http://www.jython.org",
            "http://www.youtube.com",
            "http://realpython.com",
            "http://olympus.realpython.org/dice", ] * 15

    start_time = time.time()

    request_all_urls(URLS)

    duration = time.time() - start_time
    print()
    print(f"Downloaded {len(URLS)} urls in {duration} seconds")


if __name__ == "__main__":
    main()
