import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from aiogram.filters import CommandStart
from aiogram.types import Message
import sqlite3
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
import aiohttp


class Form(StatesGroup):
    name = State()
    age = State()
    grade = State()

def init_db():
    conn = sqlite3.connect('school_data.db')
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS students (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	age INTEGER NOT NULL,
	grade TEXT NOT NULL)
	''')
    conn.commit()
    conn.close()


bot = Bot(token=TOKEN)
dp=Dispatcher()


@dp.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await message.answer('Здравствуйте, как вас зовут?')
    await state.set_state(Form.name)

@dp.message(Form.name)
async def name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Сколько вам лет?')
    await state.set_state(Form.age)

@dp.message(Form.age)
async def age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Какая ваша оценка?')
    await state.set_state(Form.grade)

@dp.message(Form.grade)
async def grade(message: Message, state: FSMContext):
    await state.update_data(grade=message.text)
    school_data = await state.get_data()

    conn = sqlite3.connect('school_data.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO students (name, age, grade) VALUES (?, ?, ?)''', (school_data['name'], school_data['age'], school_data['grade']))
    conn.commit()
    conn.close()
    await message.answer(f"Данные сохранены!\n\n"
        f"Имя: {school_data['name']}\n"
        f"Возраст: {school_data['age']}\n"
        f"Оценка: {school_data['grade']}\n\n")
    await state.clear()

async def main():
    init_db()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())