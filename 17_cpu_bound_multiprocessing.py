import time
from multiprocessing import current_process, Manager, Array, Process, freeze_support
import os


def cpu_bound(number, total_list):
    process_id = os.getpid()
    process_name = current_process().name

    # 프로세스 정보 출력
    print(f"Process ID : {process_id}, Process name : {process_name} ")
    total_list.append(sum(i * i for i in range(number)))

    return sum(i * i for i in range(number))


def main():
    numbers = [10_000_000 + x for x in range(30)]

    start_time = time.time()

    # 프로세스 리스트 선언
    processes = []
    manager = Manager()

    # 리스트 획득(프로세스 공유)
    total_list = manager.list()

    for i in numbers:
        t = Process(name=str(i), target=cpu_bound, args=(i, total_list,))
        processes.append(t)
        t.start()

    for p in processes:
        p.join()

    print(f"sum: {sum(total_list)}")

    duration = time.time() - start_time

    print(f'걸린 시간 : {duration}')


if __name__ == "__main__":
    main()
