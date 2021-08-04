# 프로세스 통신 구현 Pipe

from multiprocessing import Process, Pipe, current_process
import time
import os


# 실행함수
def worker(id, baseNum, conn):
    process_id = os.getpid()
    process_name = current_process().name

    sub_total = 0

    for i in range(baseNum):
        sub_total += 1

    # Producer
    conn.send(sub_total)
    conn.close()

    print(f'Process ID : {process_id}, Process Name : {process_name}, ID : {id}, sub_total: {sub_total}')


def main():
    parent_process_id = os.getpid()
    print(f'Parent process ID : {parent_process_id}')
    start_time = time.time()

    parent_conn, child_conn = Pipe()

    p = Process(name=str(1), target=worker, args=(1, 100000000, child_conn))
    p.start()
    p.join()
    # 순수 계산 시간
    print(f'{time.time() - start_time} seconds')

    print()
    print(f"Main-Process total count = {parent_conn.recv()}")
    print("Main Process finished")


if __name__ == "__main__":
    main()
