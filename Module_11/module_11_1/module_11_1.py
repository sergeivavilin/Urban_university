""" Для выполнения задания были выбраны библиотека requests-для работы с запросами к API
и Pillow - для работы с изображениями
С помощью библиотеки requests делаем запрос на открытый API для генерации случайных данных пользователей
После получения данных создаем список для имен и url-фото картинок пользователей.
Далее с помощью multithreading получаем сами картинки, а с помощью multiprocessing обесцвечиваем эти картинки
"""
import os
import json
from functools import wraps


import numpy as np
import pandas as pd

from datetime import datetime
from multiprocessing import Pool
from threading import Thread

import requests

from PIL import Image


def timer(func):
    """
    Декоратор для подсчета времени выполнения функции
    :param func:
    :return:
    """
    @wraps(func)
    def wrapper(*args,**kwargs):
        start_time = datetime.now()
        func(*args, **kwargs)
        end_time = datetime.now()
        print(f"Время выполнения: {end_time - start_time}")
    return wrapper


def download_picture(url_foto: str, name: str, prefix_path: str="pictures/"):
    """
    Загружаем картинку в папку pictures
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
    Получаем список с именами и url-адресами фото
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

@timer
def main(api_url: str, amount_users: int):
    # Делаем один запрос пользователей (от 1 до 5000)
    response = get_random_users(api_url, 10)
    urls_names = get_urls_names(response, 5)
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

def volatility_statistics(csv_ticker):
    df = pd.read_csv(csv_ticker)
    minimal_value_price = df["PRICE"].min()
    maximal_value_price = df["PRICE"].max()
    average_value_price = df["PRICE"].mean()
    volatility = ((maximal_value_price - minimal_value_price) / average_value_price) * 100
    secid = df.to_numpy()[0, 0]

    # print(f"Тикер: {secid}")
    # print(f"Минимальная цена: {minimal_value_price}")
    # print(f"Максимальная цена: {maximal_value_price}")
    # print(f"Средняя цена: {average_value_price}")
    # print(f"Волатильность: {volatility:.2f} %\n")
    return secid, volatility



if __name__ == '__main__':
    # api_url = 'https://randomuser.me/api/?results='
    # amount_users = 5
    # main(api_url, amount_users)
    print(os.path.abspath(os.path.curdir))


    def ticker_scrapper(dir_name: str):
        statistics = []
        for root, dirs, files in os.walk(dir_name):
            for file in files:
                if file.startswith("TICKER"):
                    ticker, volatility = volatility_statistics(os.path.join(root, file))
                    statistics.append((ticker, volatility))

        return statistics

    st = ticker_scrapper(os.path.curdir)

    st.sort(key=lambda x: x[1])
    positive_volatility = list(filter(lambda x: x[1] > 0, st))
    zero_volatility = list(filter(lambda x: x[1] == 0, st))

    three_min_volatility = [(t,round(p, 3)) for t,p in positive_volatility[:3]]
    three_max_volatility = [(t,round(p, 3)) for t,p in positive_volatility[-3:]]
    print(f"Три тикера с минимальной волатильностью: {three_min_volatility}")
    print(f"Три тикера с максимальной волатильностью: {list(reversed(three_max_volatility))}")
    print(f"Тикеры с нулевой волатильностью: {zero_volatility}")
