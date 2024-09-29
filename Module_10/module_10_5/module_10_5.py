import multiprocessing
from datetime import datetime



def read_info(name: str):
    with open(name, 'r') as f:
        all_data = f.readlines()


if __name__ == '__main__':
    file_names = ["./file 1.txt", "./file 2.txt", "./file 3.txt", "./file 4.txt"]

    # Линейная работа
    start_time = datetime.now()
    for file_name in file_names:
        read_info(file_name)
    end_time = datetime.now()
    print(f"Time for line work: {end_time - start_time}")

    # Мультипроцессорная работа
    start_time = datetime.now()
    with multiprocessing.Pool(processes=6) as pool:
        pool.map(read_info, file_names)
    end_time = datetime.now()
    print(f"Time for multiprocessing: {end_time - start_time}")

    # Результаты:
    # Time for lineal work: 0:00:01.950936
    # Time for multiprocess work: 0:00:00.753332
