import logging
from concurrent.futures import ThreadPoolExecutor
import time


class FakeDataStore:
    def __init__(self):
        # Data, Heap 영역
        self.value = 0

    def update(self, n):
        logging.info(f"Thread {n}: starting update")

        # 뮤텍스 & 락은 통한 동기화 필요
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        logging.info(f"Thread {n}: finishing update")


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread : before createing and running thread")

    store = FakeDataStore()

    logging.info(f"testing update. starting value is {store.value}")

    with ThreadPoolExecutor(max_workers=5) as executor:
        for n in ["First", "Second", "Third"]:
            executor.submit(store.update, n)

    logging.info(f"testing update. ending value is {store.value}")
