import logging
import threading


def thread_func(name, duration):
    logging.info(f"Sub-Thread {name} : start")

    for i in duration:
        print(i)

    logging.info(f"Sub-Thread {name} : finish")


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread : before creating thread")

    x = threading.Thread(target=thread_func, args=('First', range(20000)), daemon=True)
    y = threading.Thread(target=thread_func, args=("Two", range(10000)), daemon=True)
    logging.info("Main-Thread : before running thread")

    x.start()
    y.start()

    # DaemonThread 확인
    print(x.isDaemon())

    # sub thread 가 끝날 때까지 대기
    # x.join()
    # y.join()
    logging.info("Main-Thread : wait for the thread to finish")

    logging.info("Main-Thread : all done")
