import logging
from concurrent.futures import ThreadPoolExecutor
import time


def task(name):
    logging.info(f"Sub-Thread {name} : start")
    result = 0
    for i in range(10001):
        result += i
    logging.info(f"Sub-Thread {name} : finish, result = {result}")

    return result


def main():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread : before createing and running thread")

    # 실행 방법 1
    executor = ThreadPoolExecutor(max_workers=3)
    task1 = executor.submit(task, ("First",))
    task2 = executor.submit(task, ("Second",))

    print(task1.result(), task2.result())
    print()

    # 실행 방법 2 (with)
    with ThreadPoolExecutor(max_workers=3) as executor:
        tasks = executor.map(task, ["First", "Second"])

        print(list(tasks))


if __name__ == "__main__":
    main()
