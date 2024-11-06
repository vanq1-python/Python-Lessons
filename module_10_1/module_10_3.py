import threading
from random import randint
from time import sleep

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            self.lock.acquire()
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            else:
                replenishment = randint(50, 500)
                self.balance += replenishment
                print(f'Пополнение: {replenishment}. Баланс: {self.balance}')
                self.lock.release()
            sleep(0.001)


    def take(self):
        for i in range(100):
            self.lock.acquire()
            removal = randint(50, 500)
            print(f'Запророс на {removal}')
            if removal <= self.balance:
                self.balance -= removal
                print(f'Снятие: {removal}. Баланс: {self.balance}')
                self.lock.release()
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.release()
            sleep(0.001)

bk = Bank()


th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')




