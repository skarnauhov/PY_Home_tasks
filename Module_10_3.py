import threading
import time
from random import randint


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
        self.__take_running = False #флаг для отслеживания работы потока th2

    def deposit(self):
        i = 1
        while i <= 100 or self.__take_running: # необходимо, чтобы исключить зависание потока th2 по недостатку средств,
                                               # если th1 завершил работу раньше, чем th2. При этом количество пополнений > 100
        #for i in range(100):
            if self.balance > 500 and self.lock.locked():
                self.lock.release()
            a = randint(50, 500)
            self.balance += a
            time.sleep(0.01)
            print(f'\n{i}: Пополнение на сумму: {a}. Баланс: {self.balance}.')
            i += 1
        time.sleep(0.1) # без задержки почему-то успевает напечатать "Пополнение на сумму..." раньше, чем "Количество опер..".
        print(f'Количество операций пополнения: {i-1}') #чтобы оценить на сколько дольше работает th1 относительно th2

    def take(self):
        j = 0
        self.__take_running = True
        for i in range(100):
            a = randint(50, 500)
            print(f'\n{i+1}: Запрос на {a}') #f'\n - чтобы не слипалось...
            if a <= self.balance:
                self.balance -= a
                j += 1
                time.sleep(0.01)
                print(f'\n{i+1}: Снятие суммы: {a}. Баланс: {self.balance}.')
            else:
                time.sleep(0.01)
                print(f'\n{i+1}: Запрос отклонен. Недостаточно средств.')
                self.lock.acquire()
        self.__take_running = False
        time.sleep(0.1)
        print(f'Количество операций списания: {j}') # чтобы понимать сколько запросов было отклонено

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
