import concurrent.futures
import threading
import requests
import time

# 각 스레드에 생성되는 객체 (독립된 네임스페이스를 사용)
thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def request_url(url):
    session = get_session()

    # print(session)
    # print(session.headers)

    with session.get(url) as response:
        print(f'[Read Contents : {len(response.content)}, Status Code : {response.status_code} from {url}]')


def request_all_urls(urls):
    # 멀티쓰레드
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        executor.map(request_url, urls)


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
