from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

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

