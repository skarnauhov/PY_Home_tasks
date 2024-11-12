from multiprocessing import Pool
import time


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if line:
                all_data.append(line)
            else:
                break

filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов

# start_time = time.time()
# for filename in filenames:
#     read_info(filename)
# end_time = time.time()
# print(end_time-start_time)

# Многопроцессный

if __name__ == '__main__':
    start_time = time.time()
    with Pool() as process:
        process.map(read_info, filenames)
    end_time = time.time()
    print(end_time-start_time)