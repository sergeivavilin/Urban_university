from typing import Generator


def all_variants(text: str) -> Generator:
    """
    >>> list(all_variants(''))
    ['']
    >>> list(all_variants('a'))
    ['a']
    >>> list(all_variants('ab'))
    ['a', 'b', 'ab']
    >>> list(all_variants('abc'))
    ['a', 'b', 'c', 'ab', 'bc', 'abc']
    >>> list(all_variants('abcd'))
    ['a', 'b', 'c', 'd', 'ab', 'bc', 'cd', 'abc', 'bcd', 'abcd']
    """
    start_pointer = 0
    last_pointer = 0
    window= 1
    while window <= len(text):
        while last_pointer < len(text):
            yield text[start_pointer:last_pointer + 1]
            start_pointer += 1
            last_pointer += 1
        window += 1
        start_pointer = 0
        last_pointer = start_pointer + window - 1
    return


if __name__ == '__main__':
    a = all_variants("abcdefg")
    # Вызываем метод __next__
    print(f"Вызываем метод __next__ :\n{a.__next__()}")
    # Вызываем через функцию next
    print(f"Вызываем через функцию next:\n{next(a)}")
    # Продолжаем циклом for с того места где остановились
    print("Продолжаем циклом for: ")
    for i in a:
        print(i)
