import multiprocessing
import requests
import time

# 각 프로세스 메모리 영역에 생성되는 객체 (독립적)
# 함수 실행할 때마다 객체 생성은 좋지 않음 (Cost 문제) -> 미리 생성해두고 각프로세스마다 할당
session = None


def set_global_session():
    global session
    if not session:
        session = requests.Session()


def request_url(url):
    # print(session)
    # print(session.headers)

    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(
            f'[Process name : {name}, Read Contents : {len(response.content)}, Status Code : {response.status_code} from {url}]')


def request_all_urls(urls):
    # 멀티 프로세스 실행
    with multiprocessing.Pool(initializer=set_global_session, processes=1) as pool:
        pool.map(request_url, urls)


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
