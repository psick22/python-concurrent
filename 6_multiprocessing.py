from multiprocessing import Process
import time
import logging


def proc_func(name):
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info(f"Sub-Process {name} : start")
    time.sleep(3)

    logging.info(f"Sub-Process {name} : finished")


def main():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    p = Process(target=proc_func, args=("First",))
    logging.info("Main-Process : before creating Process")

    # 프로세스 시작
    p.start()

    logging.info("Main-Process : Process running")

    # logging.info("Main-Process : Terminate process")
    # p.terminate()

    logging.info("Main-Process : Process join")

    p.join()

    # 프로세스 상태 확인
    logging.info(f"Process p is alive : {p.is_alive()}")


if __name__ == "__main__":
    main()
