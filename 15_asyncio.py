import time
import asyncio


def exe_calculate_sync(name, n):
    for i in range(1, n + 1):
        print(f'{name} -> {i} of {n} is calculating...')
        time.sleep(1)
    print(f'{name} - {n} : DONE')


def process_sync():
    start_time = time.time()
    exe_calculate_sync('One', 3)
    exe_calculate_sync('Two', 2)
    exe_calculate_sync('Three', 1)

    duration = time.time() - start_time
    print(f"걸린 시간 : {duration}")


async def exe_calculate_async(name, n):
    for i in range(1, n + 1):
        print(f'{name} -> {i} of {n} is calculating...')
        await asyncio.sleep(1)
    print(f'{name} - {n} : DONE')


async def process_async():
    start_time = time.time()

    tasks = [
        asyncio.create_task(exe_calculate_async('One', 3)),
        asyncio.create_task(exe_calculate_async('Two', 2)),
        asyncio.create_task(exe_calculate_async('Three', 1))
    ]

    # 순서는 보장되지 않는다
    await asyncio.wait(tasks)
    duration = time.time() - start_time
    print(f"걸린 시간 : {duration}")


if __name__ == "__main__":
    # 1. sync 실행
    # process_sync()

    # 2. async 실행
    # 파이선 3.7이상 (asyncio.run())
    # 3.7이하 asyncio.get_event_loop().run_util_complete()
    asyncio.run(process_async())
