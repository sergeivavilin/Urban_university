from threading import Thread, Lock
from random import randint
from time import sleep


class Bank:
    AMOUNT_TRANSACTIONS = 100
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(self.AMOUNT_TRANSACTIONS):
            cur_deposit = randint(50, 500)
            self.balance += cur_deposit
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f"Пополнение: {cur_deposit}, Баланс: {self.balance}")
            sleep(0.001)

    def take(self):
        for i in range(self.AMOUNT_TRANSACTIONS):
            cur_withdraw = randint(50, 500)
            print(f"Запрос {cur_withdraw}")
            if cur_withdraw <= self.balance:
                self.balance -= cur_withdraw
                print(f"Снятие: {cur_withdraw}, Баланс: {self.balance}")
            else:
                print(f"Запрос отклонён, недостаточно средств")
                self.lock.acquire()


if __name__ == '__main__':
    bk = Bank()

    th1 = Thread(target=Bank.deposit, args=(bk,))
    th2 = Thread(target=Bank.take, args=(bk,))

    th1.start()
    th2.start()
    th1.join()
    th2.join()

    print(f'Итоговый баланс: {bk.balance}')
