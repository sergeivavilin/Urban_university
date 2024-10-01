""" Для выполнения задания были выбраны библиотеки: requests-для работы с запросами к API,
Pillow - для работы с изображениями, а также Pandas - для работы с табличными данными
и определения волатильности ценных бумаг исходя из данных в формате csv

С помощью библиотеки requests делаем запрос на открытый API для генерации случайных данных пользователей
После получения данных пользователей в формате json создаем список для имен и url-фото картинок пользователей.
Далее с помощью multithreading получаем сами картинки по полученным url-фото картинок,
а с помощью multiprocessing обесцвечиваем эти картинки.

Также с помощью библиотеки pandas формируем dataframe c данными ценных бумаг из табличных значений в виде csv-файла
После чего проводим расчеты волатильности ценных бумаг и выводим результаты
анализа по 3-м бумагам с самой высокой волатильностью, 3-м бумагам с самой низкой волатильностью и всем бумагам
с нулевой волатильности

Используя полученные навыки работы с данными библиотеками можно применять их на практике для
получения данных из разных источников с помощью запросов к API, анализировать их с помощью статистики,
а также изменять данные, полученные в виде байтовых данных (картинки)
"""
import os
from datetime import datetime
from functools import wraps
from multiprocessing import Pool
from threading import Thread
from typing import Any

import pandas as pd
import requests
from PIL import Image
from numpy import ndarray


# Декоратор для контроля времени выполнения функций
def timer(func):
    """
    Декоратор для подсчета времени выполнения функции
    :param func:
    :return:
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        function_result = func(*args, **kwargs)
        end_time = datetime.now()
        print(f"Время выполнения функции {func.__name__}(): {end_time - start_time}\n")
        return function_result

    return wrapper


# -----------------------------------------------------------------------------------------------------------------
# Часть программы для работы с графическими данными, полученными с помощью HTTP запросов

def get_random_users(api_url, amount_users: int) -> requests.Response:
    """
    Получаем данные с определенным количеством пользователей
    :param api_url: Адрес API для получения пользователей
    :param amount_users: количество пользователей
    :return: response ответ на запрос пользователей
    """
    response = requests.get(f"{api_url}{amount_users}")
    return response


def get_urls_names(response, amount_users: int) -> list:
    """
    Получаем список с именами и url-адресами фото из данных полученными через функцию get_random_users
    :param response: ответ на запрос пользователей
    :param amount_users: количество пользователей
    :return: список с именами и url-адресами фото
    """
    users_list = response.json()["results"]
    urls_names = [
        (users_list[i]["picture"]["large"],
         users_list[i]["name"]["first"] + '' + users_list[i]["name"]["last"])
        for i in range(amount_users)
    ]
    return urls_names


def download_picture(url_foto: str, name: str, prefix_path: str = "pictures/"):
    """
    Загружаем картинку в папку pictures из url адреса полученного из функции get_urls_names
    :param prefix_path: Путь до папки где будут сохранены картинки
    :param url_foto: url адрес картинки
    :param name: имя пользователя
    :return: None
    """
    data = requests.get(url_foto).content
    with open(f"{prefix_path}{name}_original.jpg", "wb") as f:
        f.write(data)


def decolorize_picture(name: str):
    """
    Обесцвечиваем картинку
    :param name: имя пользователя
    :return: None
    """
    with open(f"pictures/{name}_original.jpg", "rb") as fp:
        im = Image.open(fp).convert("L")
        im.save(f"pictures/{name}_converted.jpg")


@timer
def change_color_users_foto(api_url: str, amount_users: int):
    """
    Основная функция для изменения цвета картинок пользователей с применением потоков и процессов
    :param api_url: Адрес API для получения пользователей
    :param amount_users: количество пользователей
    :return:
    """
    # Делаем один запрос пользователей (от 1 до 5000)
    response = get_random_users(api_url, amount_users)
    urls_names = get_urls_names(response, amount_users)
    threads = []
    # Запускаем потоки для загрузки картинок
    for foto, name in urls_names:
        t = Thread(target=download_picture, args=(foto, name))
        threads.append(t)
        t.start()
    # Join-им потоки
    for thread in threads:
        thread.join()
    # Удаляем отработанные потоки
    del threads

    # Запускаем процессы обесцвечивания фото
    with Pool(processes=6) as pool:
        pool.map(decolorize_picture, [name for _, name in urls_names])

    print(f"Все фото изменены")


# -----------------------------------------------------------------------------------------------------------------
# Часть программы для анализа данных из csv файла
def volatility_statistics(csv_ticker: str) -> tuple[ndarray, int | Any]:
    """
    Рассчитывает волатильность ценных бумаг по переданному тикеру

    :param csv_ticker: путь до csv файла с тикером
    :return: secid, volatility - Кортеж из Тикера и волатильности Тикера в виде numpy массива
    """
    df = pd.read_csv(csv_ticker)
    minimal_value_price = df["PRICE"].min()
    maximal_value_price = df["PRICE"].max()
    average_value_price = df["PRICE"].mean()
    volatility = ((maximal_value_price - minimal_value_price) / average_value_price) * 100
    secid = df.to_numpy()[0, 0]

    return secid, volatility


def ticker_scrapper(dir_name: str):
    statistics = []
    for root, dirs, files in os.walk(dir_name):
        for file in files:
            if file.startswith("TICKER"):
                ticker, volatility = volatility_statistics(os.path.join(root, file))
                statistics.append((ticker, volatility))
    return statistics


@timer
def best_volatility_analyzer(dir_for_analyzer: str):
    st = ticker_scrapper(dir_for_analyzer)
    st.sort(key=lambda x: x[1])
    positive_volatility = list(filter(lambda x: x[1] > 0, st))
    zero_volatility = list(filter(lambda x: x[1] == 0, st))

    three_min_volatility = [(t, round(p, 3)) for t, p in positive_volatility[:3]]
    three_max_volatility = [(t, round(p, 3)) for t, p in positive_volatility[-3:]]

    print(f"Три тикера с минимальной волатильностью: {three_min_volatility}")
    print(f"Три тикера с максимальной волатильностью: {list(reversed(three_max_volatility))}")
    print(f"Тикеры с нулевой волатильностью: {zero_volatility}")


def main():
    # Взаимодействуем с API и меняем цвет картинок на черно-белый
    api_url = 'https://randomuser.me/api/?results='
    amount_users = 10
    change_color_users_foto(api_url, amount_users)

    # Рассчитываем волатильность ценных бумаг
    best_volatility_analyzer(os.path.abspath(os.path.curdir))


if __name__ == '__main__':
    main()
