class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name: str, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value: int):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __iadd__(self, value):
        return self.__add__(value)

    def __radd__(self, value):
        return self.__add__(value)

    def __len__(self):
        return self.number_of_floors

    def __sub__(self, other):
        if isinstance(other, House):
            other = other.number_of_floors
        self.number_of_floors -= other
        return self

    def __isub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if isinstance(other, House):
            other = other.number_of_floors
        self.number_of_floors *= other
        return self

    def __imul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, House):
            other = other.number_of_floors
        self.number_of_floors /= other
        return self

    def __floordiv__(self, other):
        if isinstance(other, House):
            other = other.number_of_floors
        self.number_of_floors //= other
        return self

    def __mod__(self, other):
        if isinstance(other, House):
            other = other.number_of_floors
        self.number_of_floors %= other
        return self

    def __pow__(self, other):
        if isinstance(other, House):
            other = other.number_of_floors
        self.number_of_floors **= other
        return self

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def go_to(self, new_floor: int):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")


if __name__ == '__main__':
    h1 = House('ЖК Эльбрус', 10)
    print(House.houses_history)
    h2 = House('ЖК Акация', 20)
    print(House.houses_history)
    h3 = House('ЖК Матрёшки', 20)
    print(House.houses_history)

    # Удаление объектов
    del h2
    del h3

    print(House.houses_history)
    # После завершения программы встроенный сборщик мусора
    # автоматически вызовет метод del для очистки последнего объекта. В нашем случае - h1, поэтому
    # будет напечатана еще одна строка : ЖК Эльбрус снесён, но он останется в истории
