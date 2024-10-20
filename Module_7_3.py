class WordsFinder:


    file_names = []

    def __init__(self, *file_names):
        self.file_names = []
        for file_name in file_names:
            self.file_names.append(file_name)

    def get_all_words(self):
        all_words = {}
        punctuation_list = ['.', ',', ':', ';', '?', '!', '=']
        tire = ['-', '—']                           # в текстах два вида тире
        for file_name in self.file_names:
            file_chars = ''
            file_words = []
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    for char in line:
                        if not char in punctuation_list: # удаление символов пунктуации, кроме тире
                            file_chars += char.lower() # создание единой строки
            file_words = list(file_chars.split())  # разделение строки на слова, тире в виде отдельных слов
            tire_positions = []
            for i in range(len(file_words)):    # создаем список позиций нахождения тире
                if file_words[i] in tire:
                    tire_positions.append(i)
            tire_positions.reverse()            # переворачиваем список
            for tire_pos in tire_positions:     # удаляем тире из списка слов начиная с большей позиции
                file_words.pop(int(tire_pos))
            all_words[file_name] = file_words
        return all_words

    def find(self, word):
        found_words = {}
        for key, value in self.get_all_words().items():
            for position in range(len(value)):
                if word.lower() == value[position]:
                    found_words[key] = position + 1
                    break
        return found_words

    def count(self, word):
        counted_words = {}
        for key, value in self.get_all_words().items():
            quantity = value.count(word.lower()) # оптимизация
            # quantity = 0
            # for position in range(len(value)):
            #     if word.lower() == value[position]:
            #         quantity += 1
            counted_words[key] = quantity
        return counted_words

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
print()

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
print()

for elem in finder1.get_all_words().items():
    print(elem)