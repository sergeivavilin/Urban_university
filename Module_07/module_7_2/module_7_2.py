def custom_write(file_name: str, strings: list[str]):
    strings_positions = {}
    number_of_strings = 1

    with open(file_name, "w", encoding="utf-8") as file:

        for string in strings:
            carriage = file.tell()
            file.write(string + "\n")
            strings_positions[(number_of_strings, carriage)] = string
            number_of_strings += 1

    return strings_positions

if __name__ == '__main__':

    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
        ]

    result = custom_write('test.txt', info)
    for elem in result.items():
      print(elem)
