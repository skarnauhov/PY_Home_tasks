import threading
import time


def write_words_to_file(word_count, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово №: {i+1}\n')
            time.sleep(0.1)
        #print(threading.current_thread())
        print(f'Запись в файл: {filename} завершена, записано: {word_count} строк.')

start_time = time.time()
write_words_to_file(10, 'example1.txt')
write_words_to_file(30, 'example2.txt')
write_words_to_file(200, 'example3.txt')
write_words_to_file(100, 'example4.txt')
end_time = time.time()
print(f'Время работы функций в секундах: {(end_time-start_time):.3f}')

thread_1 = threading.Thread(target=write_words_to_file, args=(10, 'example5.txt'))
thread_2 = threading.Thread(target=write_words_to_file, args=(30, 'example6.txt'))
thread_3 = threading.Thread(target=write_words_to_file, args=(200, 'example7.txt'))
thread_4 = threading.Thread(target=write_words_to_file, args=(100, 'example8.txt'))

start_time = time.time()
thread_1.start()
#thread_1.join()
thread_2.start()
#thread_2.join()
thread_3.start()
#thread_3.join()
thread_4.start()
#thread_4.join()

thread_1.join()
end_1_time = time.time()
print(f'Время работы потока №1 в секундах: {(end_1_time-start_time):.3f}')
thread_2.join()
end_2_time = time.time()
print(f'Время работы потока №2 в секундах: {(end_2_time-start_time):.3f}')
thread_4.join()
end_4_time = time.time()
print(f'Время работы потока №4 в секундах: {(end_4_time-start_time):.3f}')
thread_3.join()
end_3_time = time.time()
print(f'Время работы потока №3 в секундах: {(end_3_time-start_time):.3f}')

end_time = time.time()
print(f'Время работы потоков в секундах: {(end_time-start_time):.3f}')

