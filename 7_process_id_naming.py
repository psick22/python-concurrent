import random
import time
import os
from multiprocessing import Process, current_process


def square(n):
    time.sleep(random.randint(1, 3))
    process_id = os.getpid()
    process_name = current_process().name

    result = int(n) * 2
    print(f'Process ID : {process_id}, Process Name : {process_name}, results : {result}')


if __name__ == "__main__":
    # 부모 프로세스 아이디 출력
    parent_process_id = os.getpid()
    print(f'parent process ID : {parent_process_id}')

    # 프로세스 리스트 선언
    processes = list()

    # 프로세스 생성 및 실행
    for i in range(1, 100):
        t = Process(name=str(i), target=square, args=(i,))
        processes.append(t)
        t.start()

    for process in processes:
        process.join()

    # 종료
    print("Main Process Finished")
