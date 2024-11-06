import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power


    def run(self):
        print(f'{self.name}, на нас напали!')
        counter = 0
        enemis = 100
        while enemis:
            time.sleep(1)
            counter += 1
            enemis -= self.power
            print(f'{self.name} сражается {counter} день(дней,дня), осталось {enemis} воинов.')
        print(f'{self.name} одержал победу спустя {counter} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
first_knight.start()
second_knight = Knight("Sir Galahad", 20)
second_knight.start()
threads = [first_knight, second_knight]
for thread in threads:
    thread.join()

print('Все битвы закончились!')
