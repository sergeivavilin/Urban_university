from typing import Any, Iterable


def calculate_structure_sum(structure: Any)-> int:
    """
    Рекурсивная функция выводит сумму чисел и длин строк в последовательности (ограничено глубиной рекурсии)
    :param structure: Any - последовательность вложенных итерабельных структур или числа
    :return: int - Сумма чисел и длин строк в последовательности
    """
    summ = 0

    if isinstance(structure, (int, float)):
        summ += structure

    # Проверяем является ли структура итерируемой последовательностью
    elif isinstance(structure, Iterable):
        if isinstance(structure, str):
            summ += len(structure)
        elif isinstance(structure, dict):
            for substructure_key, substructure_val in structure.items():
                summ += calculate_structure_sum(substructure_key) + calculate_structure_sum(substructure_val)
        else:
            for substructure in structure:
                summ += calculate_structure_sum(substructure)

    return summ


if __name__ == "__main__":
    data_structure = [
        [1, 2, 3],
        {'a': 4, 'b': 5},
        (6, {'cube': 7, 'drum': 8}),
        "Hello",
        ((), [{(2, 'Urban', ('Urban2', 35))}])
    ]

    result = calculate_structure_sum(data_structure)
    print(result)
