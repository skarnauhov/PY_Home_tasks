import threading, queue
from time import sleep
from random import randint


class Cafe:

    def __init__(self, *tables):
        self.tables = tables
        self.queue = queue.Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            tables_guest_list = [table.guest for table in self.tables if table.guest is not None]
            if len(tables_guest_list) == len(self.tables):
                self.queue.put(guest)
                print(f'{guest.name} в очереди.')
                continue
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.table_number} и приступил(-а) к приему пищи.')
                    break

    def cater_for_guests(self):
        while True:
            sleep(1) # ждем минимальную единицу времени
            for table in self.tables:
                if table.guest is None and not self.queue.empty():
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(вышла) из очереди и сел(-а) за стол номер: '
                          f'{table.table_number} и приступил(-а) к приему пищи.')
                    table.guest.start()
                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) за {table.guest.time} секунд(ы) и ушел(ушла). '
                          f'Стол номер: {table.table_number} свободен.')
                    table.guest = None
            tables_guest_list = [table.guest for table in self.tables if table.guest is not None]
            if self.queue.empty() and len(tables_guest_list) == 0:
                print('\nВсе гости поели и ушли.')
                break


class Guest(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.time = 0

    def run(self):
        self.time = randint(3, 10)
        sleep(self.time)


class Table:

    def __init__(self, table_number, guest = None):
        self.table_number = table_number
        self.guest = guest

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.cater_for_guests()