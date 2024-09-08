"""
Задача "Всё не так уж просто":
Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Используя этот список составьте второй список primes содержащий только простые числа.
А так же третий список not_primes, содержащий все не простые числа.
Выведите списки primes и not_primes на экран(в консоль).
Пункты задачи:
Создайте пустые списки primes и not_primes.
При помощи цикла for переберите список numbers.
Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из 1ого цикла.
Отметить простоту числа можно переменной is_prime, записав в неё занчение True перед проверкой.
В процессе проверки на простоту записывайте числа из списка numbers в списки primes и not_primes
в зависимости от значения переменной is_prime после проверки (True - в prime, False - в not_prime).
Выведите списки primes и not_primes на экран(в консоль).

"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for number in numbers:
    # обработаем случаи с еденицей и двойкой отдельно
    if number < 2:
        continue
    if number == 2:
        primes.append(number)
        continue

    # Проверим если число четное то оно составное изначально
    if number % 2 == 0:
        not_primes.append(number)
        continue

    # Пройдемся по всем нечетным делителям числа от 3-х до корня из этого числа,
    for divisor in range(3, int(number ** 0.5) + 1, 2):
        if number % divisor == 0:
            not_primes.append(number)
            break
    # Если цикл закончился без прерывания то число простое
    else:
        primes.append(number)

print(f"Primes: {primes}")
print(f"Not Primes: {not_primes}")
