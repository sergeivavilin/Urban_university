from time import sleep
from typing import Optional


class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    def __init__(
            self,
            title: str,
            duration: int,
            time_now: int = 0,
            adult_mode: bool = False
    ):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users : list[User] = []
        self.videos: list[Video] = []
        self.current_user: Optional[User] = None

    def log_in(self, nickname: str, password: str):
        checked_user = self.__check_registration(nickname, password)
        if checked_user:
            self.current_user = checked_user
        else:
            print(f"Пользователь с никнеймом {nickname} не найден")

    def register(self, nickname: str, password: str, age: int):
        user_exist = self.__check_nickname(nickname)
        if not user_exist:
            temp_user = User(nickname, password, age)
            self.users.append(temp_user)
            self.current_user = temp_user
        else:
            print(f"Пользователь {nickname} уже существует")

    def log_out(self):
        self.current_user = None

    def add(self, *args: Video):
        """ Добавляем видео на платформу"""
        for item in args:
            if isinstance(item, Video) and not self.__is_video_exist(item.title):
                self.videos.append(item)

    def get_videos(self, search_word: str) -> list[str]:
        video_titles = []
        for video in self.videos:
            if video.title.lower().__contains__(search_word.lower()):
                video_titles.append(video.title)
        return video_titles

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        current_video = self.__get_concrete_video(title)
        if not current_video:
            # Здесь можно вывести что видео не найдено
            return

        permission_for_this_video = self.__is_user_adult_for_video(current_video.adult_mode, self.current_user.age)
        if permission_for_this_video:
            for sec in range(1, current_video.duration + 1):
                sleep(1)
                print(sec, end=" ")
            print("Конец видео")
        else:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")

    def __is_user_adult_for_video(self, video_adult_mode: bool, age: int) -> bool:
        if video_adult_mode and age >= 18:
            return True
        elif video_adult_mode and age < 18:
            return False
        else:
            return True

    def __check_nickname(self, nickname, get_user=False) -> bool or User:
        for user in self.users:
            if user.nickname.lower() == nickname.lower():
                if get_user:
                    return user
                return True
        return False

    def __check_registration(self, nickname: str, password: str) -> Optional[User]:
        user = self.__check_nickname(nickname, get_user=True)
        if user and hash(password) == user.password:
            return user
        return None

    def __is_video_exist(self, title: str, get_video: bool = False) -> bool or Video:
        for video in self.videos:
            if video.title.lower() == title.lower():
                if get_video:
                    return video
                return True
        return False

    def __get_concrete_video(self, title) -> Optional[Video]:
        video = self.__is_video_exist(title, get_video=True)
        if video:
            return video
        return None


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
