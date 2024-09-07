#  Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"

immutable_var = (1, "string", [1, 2, 3])
print(immutable_var)  # (1,'string', [1, 2, 3])

mutable_list = [1, 2, 3]
mutable_list.remove(1)
mutable_list[0] = 0

print(mutable_list)  # [0, 3]
