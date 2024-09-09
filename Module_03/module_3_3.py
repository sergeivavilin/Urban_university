def print_params(a = 1, b = 'строка', c = True):
    print(f"Аргумент a: {a}, Аргумент b: {b}, Аргумент c: {c}")

print("Функция с параметрами по умолчанию:")
print_params()
print_params(b = 25)
print_params(c = [1,2,3])


print("\nРаспаковка параметров:")
values_list = [2, "MAIL", (True, False, None)]
values_dict = {"a": 3, "b": ["Home", "Tree"], "c": {"d": "UNEXPECTED"}}

print_params(*values_list)
print_params(**values_dict)

print("\Распаковка + отдельные параметры:")
values_list_2 = [True, (1,)]

print_params(*values_list_2, 42) # работает но так лучше не делать)
