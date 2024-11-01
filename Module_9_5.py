class StepValueError(ValueError):

    def __init__(self, message):
        self.message = message


class Iterator:

    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError('Шаг не может быть равен 0')
        else:
            self.step = step
        self.start = start
        self.stop = stop
        self.pointer = start

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if self.step > 0 and self.pointer > self.stop:
            raise StopIteration
        if self.step < 0 and self.pointer < self.stop:
            raise StopIteration
        if self.pointer == self.start:
            self.pointer += self.step
            return self.start
        else:
            self.pointer += self.step
            return self.pointer - self.step

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError as exc:
        print(exc.message)
print('*'*20)

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


for i in iter2:
    print(i, end=' ')
print()
print('*'*20)
for i in iter3:
    print(i, end=' ')
print()
print('*'*20)
for i in iter4:
    print(i, end=' ')
print()
print('*'*20)
for i in iter5:
    print(i, end=' ')
print()
print('*'*20)




