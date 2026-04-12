import asyncio
from aiogram import Bot, Dispatcher, F
from config import TOKEN
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, FSInputFile
from deep_translator import GoogleTranslator

bot = Bot(token=TOKEN)
dp=Dispatcher()
translator = GoogleTranslator(source="auto", target="en")

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Здравствуйте, я бот-погода')

async def main():
    await dp.start_polling(bot)


@dp.message(Command('help'))
async def help(message: Message):
    await message.answer("Этот бот умеет выполнять: \n /start - начать разговор \n /help - показать все доступные команды \n /voice - отправить голосовое сообщение s.mp3 в Telegram \n Также бот умеет отправлять ваши картинки в файл img и переводит ваши английские слова в русские" )

@dp.message(F.photo)
async def photo(message: Message):
    await bot.download(message.photo[-1],destination=f'img/{message.photo[-1].file_id}.jpg')

@dp.message(Command('voice'))
async def react_voice(message: Message):
    voice=FSInputFile('s.mp3')
    await message.answer_voice(voice)


@dp.message(F.text & ~F.text.startswith('/'))
async def translate_text(message: Message):
    original_text = message.text.strip()
    if not original_text:
        return

    try:
        translated = translator.translate(original_text)
        await message.answer(f" Перевод на английский:\n{translated}")
    except Exception:
        await message.answer("Не удалось перевести текст. Проверьте подключение к интернету.")

if __name__ == "__main__":
    asyncio.run(main())