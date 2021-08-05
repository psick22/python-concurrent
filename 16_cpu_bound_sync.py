import time


def cpu_bound(number):
    return sum(i * i for i in range(number))


def find_sums(numbers):
    result = []
    for number in numbers:
        result.append(cpu_bound(number))

    return result


def main():
    numbers = [10_000_000 + x for x in range(30)]

    start_time = time.time()

    total = find_sums(numbers)

    print(f"sum: {sum(total)}")

    duration = time.time() - start_time

    print(f'걸린 시간 : {duration}')


if __name__ == "__main__":
    main()
