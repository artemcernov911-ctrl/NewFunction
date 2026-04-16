from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

test = ["Привет", "Пока"]

async def test_keyboard():
    keyboard = InlineKeyboardBuilder()
    for key in test:
        keyboard.add(InlineKeyboardButton(text=key, callback_data=key))
    return keyboard.adjust(2).as_markup()


inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Новости',url='https://university.zerocoder.ru/pl/teach/control/lesson/view?id=343780948')],
[InlineKeyboardButton(text='Музыка',url='https://university.zerocoder.ru/pl/teach/control/lesson/view?id=343780948')],
[InlineKeyboardButton(text='Видео',url='https://university.zerocoder.ru/pl/teach/control/lesson/view?id=343780948')]
])

async def show_more():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="Показать больше", callback_data="show_more"))
    return keyboard.adjust(1).as_markup()

async def options_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="Опция 1", callback_data="option_1"))
    keyboard.add(InlineKeyboardButton(text="Опция 2", callback_data="option_2"))
    return keyboard.adjust(2).as_markup()

