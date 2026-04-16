import asyncio
from aiogram import Bot, Dispatcher, F
from config import TOKEN
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
import keyboard as kb

bot = Bot(token=TOKEN)
dp=Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Здравствуйте, я бот', reply_markup=await kb.test_keyboard())

async def main():
    await dp.start_polling(bot)


@dp.callback_query(F.data == "Привет")
async def process_hello_button(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(f"Привет, {callback.from_user.first_name}!")

@dp.callback_query(F.data == "Пока")
async def process_goodbye_button(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(f"Пока, {callback.from_user.first_name}!")

@dp.message(Command("links"))
async def links(message: Message):
   await message.answer("Выбирай", reply_markup=kb.inline_keyboard)

@dp.message(Command("dynamic"))
async def dynamic_start(message: Message):
    await message.answer("Нажмите кнопку ниже:", reply_markup=await kb.show_more())


@dp.callback_query(F.data == "show_more")
async def process_show_more(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_reply_markup(reply_markup=await kb.options_keyboard())

@dp.callback_query(F.data == "option_1")
async def process_option_1(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(f"Вы выбрали Опцию 1, {callback.from_user.first_name}!")

@dp.callback_query(F.data == "option_2")
async def process_option_2(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(f"Вы выбрали Опцию 2, {callback.from_user.first_name}!")


if __name__ == "__main__":
    asyncio.run(main())