# 프로세스 통신 구현 Queue

from multiprocessing import Process, Queue, current_process
import time
import os


# 실행함수
def worker(id, baseNum, q):
    process_id = os.getpid()
    process_name = current_process().name

    sub_total = 0

    for i in range(baseNum):
        sub_total += 1

    # Producer
    q.put(sub_total)

    print(f'Process ID : {process_id}, Process Name : {process_name}, ID : {id}, sub_total: {sub_total}')


def main():
    parent_process_id = os.getpid()
    print(f'Parent process ID : {parent_process_id}')
    processes = []
    start_time = time.time()

    q = Queue()

    for i in range(4):
        p = Process(name=str(i), target=worker, args=(i, 100000000, q))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    # 순수 계산 시간
    print(f'{time.time() - start_time} seconds')

    q.put('exit')

    total = 0
    while True:
        tmp = q.get()
        if tmp == 'exit':
            break
        else:
            total += tmp

    print()
    print(f"Main-Process total count = {total}")
    print("Main Process finished")


if __name__ == "__main__":
    main()
