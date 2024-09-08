#  Практическое задание по теме: "Словари и множества"

# Работа со словарями
my_dict = {"Vasya": 1975, "Egor": 1999, "Masha": 2002}

print(f"Dict: {my_dict}")
print(f"Existing value: {my_dict.get("Masha")}")
print(f"Not existing value: {my_dict.get("Lena")}")

my_dict.update({"Kamila": 1981, "Artem": 1915})

print(f"Deleted value: {my_dict.pop("Egor")}")
print(f"Modified dictionary: {my_dict}\n")

# Работа с множествами

my_set = {1, "Яблоко", 42.314, 1, "Яблоко"}

print(f"Set: {my_set}")

my_set.discard(1)
my_set.update([13], {(5, 6, 1.6)})

print(f"Modified set: {my_set}")
