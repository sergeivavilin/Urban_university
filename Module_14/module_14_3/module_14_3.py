import asyncio
import os

from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import CommandStart
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, CallbackQuery, FSInputFile, InputMediaPhoto
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder, KeyboardButton

# Создаем бота, токен лучше хранить в переменной окружения
# или использовать файл .env и библиотеки для работы с переменными (python-dotenv, decouple и т.д.)
# в данном проекте использована библиотека python-dotenv (https://github.com/theskumar/python-dotenv)
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()

bot = Bot(token=os.environ.get("BOT_TOKEN"))
# Инициализируем диспатчер
dp = Dispatcher(storage=MemoryStorage())
# Создаем базовый роутер (в версии 3.x используется либо Router().message, либо dp.message вместо dp.message_handler)
base_router = Router()

# Прописываем путь до папки с картинками
all_media_dir = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "all_media"))

# Создаем медиа группу для картинок всех товаров
photo_list = []
for number, file in enumerate(os.listdir(all_media_dir), start=1):
    photo_file = InputMediaPhoto(
        type="photo",
        media=FSInputFile(os.path.join(all_media_dir, file)),
        caption=f"Название: Product {number} | Описание: описание {number} | Цена: {number * 100}"
    )
    photo_list.append(photo_file)

# Создаем состояния пользователя
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


# Создаем клавиатуры
# Стартовая клавиатура
kb = ReplyKeyboardBuilder()
# Устанавливаем максимальное количество кнопок в строке
kb.max_width = 2  
kb.row(
    KeyboardButton(text="Рассчитать"),
    KeyboardButton(text="Информация"),
    KeyboardButton(text="Купить")
)

# Инлайн клавиатура для расчета калорий
inline_formulas = InlineKeyboardBuilder()
inline_formulas.button(text="Формулы расчёта", callback_data="formulas")
inline_formulas.button(text="Рассчитать норму калорий", callback_data="calories")

# Инлайн клавиатура для покупки
inline_buy_menu = InlineKeyboardBuilder()
inline_buy_menu.max_width = 4  # Устанавливаем максимальную ширину
inline_buy_menu.button(text="Product1", callback_data="product_buying")
inline_buy_menu.button(text="Product2", callback_data="product_buying")
inline_buy_menu.button(text="Product3", callback_data="product_buying")
inline_buy_menu.button(text="Product4", callback_data="product_buying")


# Класс CommandStart обрабатывает только на команду /start.
@base_router.message(CommandStart())
async def start(message: Message):
    # При вводе команды /start отправляем клавиатуру, которая будет подстраиваться под размеры интерфейса
    await message.answer(
        text=f"Привет! {message.from_user.full_name}! Я бот помогающий твоему здоровью.",
        reply_markup=kb.as_markup(resize_keyboard=True, one_time_keyboard=True)
    )


# Отлавливаем сообщения с текстом "купить" и отправляем inline клавиатуру с товарами
# Для удобства восприятия картинки отправляем в сформированной заранее медиа группе (photo_list)
@base_router.message(F.text.lower().contains("купить"))
async def get_buying_list(message: Message):
    await message.answer_media_group(media=photo_list)
    await message.answer(text="Выберите товар", reply_markup=inline_buy_menu.as_markup(resize_keyboard=True))


# Отлавливаем сообщения с текстом "рассчитать" и отправляем inline клавиатуру
@base_router.message(F.text.lower().contains("рассчитать"))
async def inline_menu(message: Message):
    await message.answer(text=f"Выберите опцию: ", reply_markup=inline_formulas.as_markup(resize_keyboard=True))


# Отлавливаем callback сообщения с текстом "product_buying"
# Теперь у магического фильтра F мы должны использовать data вместо text
@dp.callback_query(F.data.contains("product_buying"))
async def send_confirm_message(call: CallbackQuery):
    await call.message.answer(f"Вы успешно приобрели продукт!")


# Отлавливаем callback сообщения с текстом "formulas"
# Теперь у магического фильтра F мы должны использовать data вместо text
@dp.callback_query(F.data.contains("formulas"))
async def get_formulas(call: CallbackQuery):
    await call.message.answer(text=f"10 x вес(кг) + 6.25 x рост(см) - 5 x возраст(лет) - 161")


# Отлавливаем callback сообщения с текстом "calories"
@base_router.callback_query(F.data.contains("calories"))
async def set_age(call: CallbackQuery, state: FSMContext):
    await call.message.answer(f"Введите свой возраст: ")
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
