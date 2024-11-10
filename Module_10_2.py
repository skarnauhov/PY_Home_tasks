import threading
import time


class Knight(threading.Thread):

    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self._enemy_power = 100

    def __fight(self):
        battle_duration = 0
        while self._enemy_power > 0:
            time.sleep(1)
            battle_duration += 1
            self._enemy_power -= self.power
            print(f'{self.name} сражается {battle_duration} день(дня)..., осталось {self._enemy_power} воинов.')
        print(f'{self.name} одержал победу, спустя {battle_duration} дней!')

    def run(self):
        print(f'{self.name} на нас напали!')
        self.__fight()

# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
# Вывод строки об окончании сражения
print('Все битвы закончились')