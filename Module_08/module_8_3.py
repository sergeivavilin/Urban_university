class Car:
    def __init__(self, model: str, vin: int, number: str):
        self.model = model
        self.__vin = vin if self.__is_valid_vin(vin) else None
        self.__number = number if self.__is_valid_numbers(number) else None

    def __is_valid_vin(self, vin: int) -> bool:
        if not isinstance(vin, int):
            raise IncorrectVinNumber(message="Некорректный тип vin номер")
        if not 1_000_000 <= vin <= 9_999_999:
            raise IncorrectVinNumber(message="Неверный диапазон для vin номера")
        return True

    def __is_valid_numbers(self, number):
        if not isinstance(number, str):
            raise IncorrectCarNumbers(message="Некорректный тип данных для номеров")
        if len(number) != 6:
            raise IncorrectCarNumbers(message="Некорректная длина номера")
        return True


class IncorrectVinNumber(Exception):
    def __init__(self, message: str):
        super().__init__()
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message: str):
        super().__init__()
        self.message = message


if __name__ == '__main__':
    try:
        first = Car('Model1', 1000000, 'f123dj')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{first.model} успешно создан')

    try:
        second = Car('Model2', 300, 'т001тр')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{second.model} успешно создан')

    try:
        third = Car('Model3', 2020202, 'нет номера')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{third.model} успешно создан')
