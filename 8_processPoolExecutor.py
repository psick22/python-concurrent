from concurrent.futures import ProcessPoolExecutor, as_completed
import urllib.request

URLS = [
    'http://www.naver.com',
    'http://www.google.com',
    'http://www.youtube.com',
    'http://www.naver.com',
    'http://www.google.com',
    'http://www.youtube.com',
    'http://www.naver.com',
    'http://www.google.com',
    'http://www.youtube.com',
    'http://www.naver.com',
    'http://www.google.com',
    'http://www.youtube.com',
    'http://www.naver.com',
    'http://www.google.com',
    'http://www.youtube.com',
]


def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

    pass


def main():
    # 프로세스풀 컨텍스트 영역
    with ProcessPoolExecutor(max_workers=20) as executor:
        # Future 로드(실행 x)
        future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}

        print(future_to_url)

        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as e:
                print(f'{url} generated an exception : {e}')
            else:
                print(f'{url} page is {len(data)} bytes')

    pass


if __name__ == "__main__":
    main()
