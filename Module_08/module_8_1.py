def add_everything_up(a: (int or float) or str, b: (int or float) or str):
    try:
        result = a + b
        return f"{result:.3f}"
    except (TypeError, ValueError):
        return f"{a}{b}"


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print(add_everything_up("d", "3"))
print(add_everything_up(["d"], {"3": 3}))
