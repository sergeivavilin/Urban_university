from threading import Thread
from time import sleep


class Knight(Thread):
    amount_enemies = 100

    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        print(f"{self.name} на нас напали")
        enemies_left = Knight.amount_enemies
        days = 0

        while enemies_left > 0:
            sleep(1)
            days += 1
            enemies_left -= self.power
            print(f"{self.name}, сражается {days} день ..., осталось {enemies_left} воинов.")

        print(f"{self.name} одержал победу спустя {days} дней(дня)!")


if __name__ == '__main__':
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)

    knight_list = [first_knight, second_knight]

    for knight in knight_list:
        knight.start()

    for knight in knight_list:
        knight.join()

    print("Все битвы закончились!")
