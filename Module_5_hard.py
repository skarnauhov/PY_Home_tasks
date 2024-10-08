from time import sleep


class User:
    """
    Класс User (пользователь сервиса UrTube), обладает атрибутами: nickname, password, age
    """

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = int(age)

    def __gt__(self, other):
        if isinstance(other, User):
            return self.age > other.age
        elif isinstance(other, int):
            return self.age > other
        else:
            return NotImplemented

    def __str__(self):
        return self.nickname


class Video:
    """
    Класс Video, обладает атрибутами: title, duration, time_now, adult_mode
    """

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = int(duration)
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, other):
        if isinstance(other, Video):
            return self.title == other.title
        elif isinstance(other, str):
            return self.title is other
        else:
            return NotImplemented

    def __str__(self):
        return self.title


class UrTube:

    """
    Класс UrTube - видеохостинг, содержит в себе: список объектов класса User,
    список объектов класса Video, позволяет работать с этими классами разными методами.
    """

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self,nickname, password):
        user_found = False
        if len(self.users) < 1:
            print('Пользователь не найден.')
        else:
            for user in self.users:
                if user.nickname == nickname and user.password == hash(password):
                    user_found = True
                    self.current_user = user
            if not user_found:
                print('Пользователь не найден.')

    def log_out(self):
        self.current_user = None

    def register(self,nickname, password, age):
        same_user = False
        if len(self.users) < 1:
            self.users.append(User(nickname, password, age))
            self.log_in(nickname, password)
        else:
            for user in self.users:
                if user.nickname == nickname:
                    same_user = True
            if same_user:
                print(f"Пользователь {nickname} уже существует")
            else:
                self.users.append(User(nickname,password,age))
                self.log_in(nickname,password)

    def add(self, *videos):
        for video in videos:
            new_video = True
            for v in range(len(self.videos)):
                if video == self.videos[v]:
                    new_video = False
            if new_video:
                self.videos.append(video)

    def get_videos(self, search_string):
        search_result = []
        for v in range(len(self.videos)):
            if search_string.lower() in self.videos[v].title.lower():
                search_result.append(str(self.videos[v]))
        return search_result

    def watch_video(self, video_title):
        if self.current_user is not None:
            for v in range(len(self.videos)):
                if video_title == self.videos[v]:
                    if self.videos[v].adult_mode and self.current_user.age > 18:
                        for second in range(self.videos[v].duration):
                            print(second + 1, end=' ')
                            sleep(1)
                        print('Конец видео')
                    else:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
