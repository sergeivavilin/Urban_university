from datetime import datetime
from time import sleep
from functools import wraps
from threading import Thread


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        func(*args, **kwargs)
        end = datetime.now()
        print(f"Выполнение функции: {func.__name__} заняло: {end - start} секунд\n")
    return wrapper


def write_words(word_count: int, file_name: str):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

@timer
def without_threads():
    test_cases = [
        (10, "example1.txt"),
        (30, "example2.txt"),
        (200, "example3.txt"),
        (100, "example4.txt")
    ]

    for test_case in test_cases:
        write_words(test_case[0], test_case[1])

@timer
def with_threads():
    test_cases = [
        (10, "example5.txt"),
        (30, "example6.txt"),
        (200, "example7.txt"),
        (100, "example8.txt")
    ]

    threads = []
    for test_case in test_cases:
        threads.append(Thread(target=write_words, args=test_case))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    print("\nЗапуск без потоков")
    without_threads()

    print("\nЗапуск с потоками")
    with_threads()
