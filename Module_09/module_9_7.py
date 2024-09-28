def is_prime(func):
    def wrapper(*args):
        number = func(*args)

        if number == 2:
            prime = True
        # Проверим если число четное, то оно составное изначально
        elif number < 2 or number % 2 == 0:
            prime = False

        else:
            # Пройдемся по всем нечетным делителям числа от 3-х до корня из этого числа,
            # Если цикл закончился без прерывания, то число простое
            for divisor in range(3, int(number ** 0.5) + 1, 2):
                if number % divisor == 0:
                    prime = False
                    break
            else:
                prime = True

        print(f"{'Простое' if prime else 'Составное'}")
        return number
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


if __name__ == '__main__':

    result = sum_three(2, 3, 6)
    print(result)
    # Можно передавать любое количество чисел, но не обязательно)
    result = sum_three(2, 3, 6, 7, 8)
    print(result)
