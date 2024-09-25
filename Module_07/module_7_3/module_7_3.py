
class WordsFinder:
    punctuation = [",", ".", "=", "!", "?", ";", ":", " - "]

    def __init__(self,*name_files: str):
        self.name_files: tuple[str, ...] = name_files
        self.__all_words: dict[str: list[str]] = self.get_all_words()

    def get_all_words(self) -> dict[str: list[str]]:
        all_words = {}

        for name_file in self.name_files:
            with open(name_file, 'r', encoding='utf-8') as file:
                all_words[name_file] = []
                # Построчно читаем файл
                for line in file:
                    # Убираем пунктуацию из строки
                    clear_string = self.__replace_punctuation(line)
                    words_in_line = clear_string.split()
                    all_words[name_file].extend(words_in_line)
        return all_words

    def find(self, word):
        all_words: dict[str: list[str]] = self.__all_words
        founded_word = {}

        for name_file, words in all_words.items():
            if word.lower() in words:
                founded_word[name_file] = words.index(word.lower()) + 1

        return founded_word

    def count(self, word):
        all_words: dict[str: list[str]] = self.__all_words
        founded_word = {}

        for name_file, words in all_words.items():
            count_word = words.count(word.lower())
            if count_word > 0:
                founded_word[name_file] = count_word

        return founded_word

    def __replace_punctuation(self, string_for_replace: str) -> str:
        clear_string = string_for_replace.lower()
        for sym in self.punctuation:
            clear_string = clear_string.replace(sym, "")
        return clear_string


if __name__ == '__main__':


    finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                          'Rudyard Kipling - If.txt',
                          'Mother Goose - Monday’s Child.txt')
    print(finder1.get_all_words())
    print(finder1.find('the'))
    print(finder1.count('the'))
    print()
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words()) # Все слова
    print(finder2.find('TEXT')) # 3 слово по счёту
    print(finder2.count('teXT')) # 4 слова teXT в тексте всего

