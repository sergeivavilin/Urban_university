def divide(first, second):
    try:
        result = first / second
    except ZeroDivisionError:
        result = float("inf")
    return result

