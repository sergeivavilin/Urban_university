def personal_sum(numbers):
    incorrect_data = 0
    summ = 0

    for i in numbers:
        try:
            summ += i
        except TypeError:
            incorrect_data += 1
            print(f"Некорректный тип данных для подсчёта суммы - {i}")

    return summ, incorrect_data


def calculate_average(numbers):
    try:
        sum_of_numbers, incorrect_data = personal_sum(numbers)
    except TypeError:
        print("В numbers записан некорректный тип данных")
        return

    try:
        result = sum_of_numbers / (len(numbers) - incorrect_data)
    except ZeroDivisionError:
        result = 0

    return result


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
