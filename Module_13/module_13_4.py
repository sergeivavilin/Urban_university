import asyncio

from aiogram import Bot, Dispatcher, Router, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message
from aiogram.filters import CommandStart

from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup

# Создаем бота, токен лучше хранить в переменной окружения
# или использовать файл .env и библиотеки для работы с переменными (python-dotenv, decouple и т.д.)
bot = Bot(token="BOT_TOKEN")
# Инициализируем диспатчер
dp = Dispatcher(storage=MemoryStorage())
# Создаем базовый роутер (в версии 3.x используется Router() вместо dp.message_handler)
base_router = Router()

# Создаем состояния пользователя
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


# Класс CommandStart обрабатывает только команду /start.
@base_router.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Привет! {message.from_user.full_name}! Я бот помогающий твоему здоровью.")

# Отлавливаем сообщения с текстом calories
@base_router.message(F.text.lower().contains("calories"))
async def set_age(message: Message, state: FSMContext):
    await message.answer(f"{message.from_user.full_name} введите свой возраст: ")
    # Переводим пользователя в следующее состояние
    await state.set_state(UserState.age)


@base_router.message(UserState.age)
async def set_growth(message: Message, state: FSMContext):
    # Сохраняем данные пользователя
    await state.update_data(age=message.text)
    await message.answer(f"Введите свой рост: ")
    # Переводим пользователя в следующее состояние
    await state.set_state(UserState.growth)

@base_router.message(UserState.growth)
async def set_weight(message: Message, state: FSMContext):
    # Сохраняем данные пользователя
    await state.update_data(growth=message.text)
    await message.answer(f"Введите свой вес: ")
    # Переводим пользователя в следующее состояние
    await state.set_state(UserState.weight)

@base_router.message(UserState.weight)
async def send_calories(message: Message, state: FSMContext):
    # Сохраняем данные пользователя
    await state.update_data(weight=message.text)
    # получаем все данные пользователя в виде словаря
    data = await state.get_data()
    # вычисляем норму калорий
    man_calories = 10 * int(data["weight"]) + 6.25 * int(data["growth"]) - 5 * int(data["age"]) + 5
    await message.answer(f"Ваша норма калорий: {man_calories} ккал")
    # Сбрасываем состояния пользователя
    await state.clear()

# Если оставить роутер без аргументов, то он будет отлавливать все необработанные ранее сообщения
@base_router.message()
async def all_massages(message: Message):
    await message.answer(f"Введите команду /start, чтобы начать общение.")

# Основная асинхронная функция. Добавляем роутер в диспатчер и запускаем его.
async def main():
    dp.include_router(base_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
