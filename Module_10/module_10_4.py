from datetime import datetime
from random import randint
from threading import Thread
from time import sleep
from queue import Queue


class Guest(Thread):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def run(self):
        time_for_lunch = randint(3, 10)
        sleep(time_for_lunch)

class Table:
    def __init__(self, number: int, guest: Guest = None):
        self.number = number
        self.guest = guest


class Cafe:
    def __init__(self, *tables: Table):
        self.tables = tables
        self.queue_guests = Queue()

    def __tables_empty(self):
        for table in self.tables:
            if table.guest is not None:
                return False
        return True

    def __fill_queue(self, *guests):
        for guest in guests:
            self.queue_guests.put(guest)

    def __fill_tables(self):
        if self.queue_guests.empty():
            return

        vacant_tables = [table for table in self.tables if table.guest is None]

        if vacant_tables:
            for table in vacant_tables:
                table.guest = self.queue_guests.get()
                print(f'{table.guest.name} сел(-а) за стол номер {table.number}')
                table.guest.start()

            for guest in self.queue_guests.queue:
                print(f"{guest.name} в очереди")
            print()

    def guest_arrival(self, *guests):
        # Добавление гостей в очередь
        self.__fill_queue(*guests)
        # Заполнение пустых столов гостями из очереди
        self.__fill_tables()

    def discuss_guests(self):
        while not self.queue_guests.empty() or not self.__tables_empty():
            # Проверяем столы на наличие гостей, которые закончили кушать
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None
                    self.__fill_tables()

        print("\nОбслуживание гостей выполнено")

if __name__ == '__main__':
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]
    # Имена гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]
    # Создание гостей
    guests = [Guest(name) for name in guests_names]

    ts = datetime.now()
    # Заполнение кафе столами
    cafe = Cafe(*tables)
    # Приём гостей
    cafe.guest_arrival(*guests)
    # Обслуживание гостей
    cafe.discuss_guests()
    te = datetime.now()
    # Вывод времени обслуживания гостей
    print(f'Время обслуживания гостей: {te - ts}')
