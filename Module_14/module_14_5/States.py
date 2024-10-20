from aiogram.fsm.state import StatesGroup, State


# Создаем состояния пользователя
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()
