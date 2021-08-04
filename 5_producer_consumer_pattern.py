from concurrent.futures import ThreadPoolExecutor
import logging
import queue
import random
import threading
import time


def producer(queue, event):
    """ 네트워크 대기상태라 가정(서버) 주로 I/O 작업을 통해 데이터 Read """
    while not event.is_set():
        message = random.randint(1, 11)
        logging.info(f'Producer create message: {message}')
        queue.put(message)

    logging.info(f"Producer recevied event exit")


def consumer(queue, event):
    """ 데이터를 응답 받고 처리 하여 DB 저장 """
    while not event.is_set() or not queue.empty():
        message = queue.get()
        logging.info(f"Consumer storing message : {message} (size={queue.qsize()})")

    logging.info("Consumer received event exit")


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread : before creating and running thread")

    pipeline = queue.Queue(maxsize=10)

    # 이벤트 플래그
    event = threading.Event()

    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        # 실행 시간 조정
        time.sleep(1)

        logging.info("Main: about to set event")

        # 프로그램 종료
        event.set()
