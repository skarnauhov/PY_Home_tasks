class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        running_runners = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                running_runners[str(participant)] = participant.distance
            running_distances = list(running_runners.values())
            if max(running_distances) >= self.full_distance:
                i = running_distances.index(max(running_distances))
                participant = self.participants[i]
                finishers[place] = participant
                place += 1
                self.participants.remove(participant)
                running_runners.__delitem__(str(participant))
                participant.__init__(str(participant), speed = participant.speed) # инициализация
                # позволяет проводить соревнования с одними и теми же спортсменами подряд несколько раз, обнуляя пройденное расстояние
        return finishers

first = Runner('Вася', 10)
second = Runner('Илья', 5)
third = Runner('Арсен', 10)

t = Tournament(101, first, third)
print(t.start())
t = Tournament(157, second, third)
print(t.start())
t = Tournament(89, first, second, third)
print(t.start())