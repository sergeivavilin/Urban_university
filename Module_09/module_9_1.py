from typing import Callable


def apply_all_func(int_list: list[int or float], *functions: Callable):

    result = {}
    for func in functions:
        try:
            result[func.__name__] = func(int_list)
        except TypeError as e:
            print(f"Получена ошибка типа данных: {e} в функции {func.__name__}")
        except ValueError as e:
            print(f"Получена ошибка значения данных: {e} в функции {func.__name__}")

    return result


if __name__ == '__main__':

    def some_func(*some_args):
        pass

    print(apply_all_func([6, 20, 15, 9], max, min))
    print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
    print(apply_all_func(1, len, sum, sorted))
    print(apply_all_func([6, 20, 15, "9"], len, sorted))
    print(apply_all_func({}, max, min))
    print(apply_all_func([], some_func))
