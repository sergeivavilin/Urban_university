def divide(first, second):
    try:
        result = first / second
    except ZeroDivisionError:
        result = "Ошибка"
    return result
