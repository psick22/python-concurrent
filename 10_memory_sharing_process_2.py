from multiprocessing import Process, current_process, Value, Array
import os


# 공유되는 경우

def generate_update_number(v):
    for _ in range(50):
        v.value += 1
    print(current_process().name, "data", v)


def main():
    # 부모 프로세스 아이디
    parent_process_id = os.getpid()
    print(f'Parent Process ID : {parent_process_id}')

    processes = []

    # 프로세스 메모리 공유 변수
    # from multiprocessing import shared_memory 사용가능
    # from multiprocessing import Manager 사용가능
    # share_array = Array('i', range(50))
    share_value = Value('i', 0)

    for _ in range(1, 10):
        p = Process(target=generate_update_number, args=(share_value,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f"share_value가 프로세스간에 공유되었다면 {50 * len(processes)} 이어야함 :: {share_value}")


if __name__ == "__main__":
    main()
