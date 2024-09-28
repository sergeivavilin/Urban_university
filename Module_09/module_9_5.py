class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = self.start

    def __iter__(self):
        if self.step == 0:
            raise StepValueError
        self.pointer = self.start
        return self

    def __next__(self):
        previous = self.pointer
        if self.__step_positive() or self.__step_negative():
            self.pointer += self.step
        else:
            raise StopIteration
        return previous

    def __step_positive(self):
        if self.step > 0 and self.pointer <= self.stop:
            return True
        return False

    def __step_negative(self):
        if self.step < 0 and self.pointer >= self.stop:
            return True
        return False


if __name__ == '__main__':
    try:
        iter1 = Iterator(100, 200, 0)
        for i in iter1:
            print(i, end=' ')
    except StepValueError:
        print('Шаг указан неверно')

    iter2 = Iterator(-5, 1)
    iter3 = Iterator(6, 15, 2)
    iter4 = Iterator(5, 1, -1)
    iter5 = Iterator(10, 1)
    iter6 = Iterator(-1, -5, -1)

    for iterator in [iter2, iter3, iter4, iter5, iter6]:

        for i in iterator:
            print(i, end=' ')
        print()

