import string
import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

API = '5872804799:AAEQqg5oEbYUcoqGQ4kWrH8a0TaFTCkz1F0'
HELP = '''/start - начать работу
/help - список функций
/reverse - написать строку в обратном порядке
/capitalize - написать строку заглавными буквами
/lower - написать строку строчными буквами
/random_letter - вывести рандомную букву латинского алфавита
/random_number - вывести рандомное число от 1 до 100'''
STORAGE = MemoryStorage()
bot = Bot(API)
dp = Dispatcher(bot, storage=STORAGE)


class Form(StatesGroup):
    ans = State()
    ans2 = State()
    ans3 = State()


@dp.message_handler(commands=['help'])
async def com_help(message: types.Message):
    await message.answer(text=HELP)
    await message.delete()


@dp.message_handler(commands=['start'])
async def com_start(message: types.Message):
    await message.answer(text='Бот подключен! Чтобы узнать, что он умеет, напишите /help')


@dp.message_handler(commands=['reverse'])
async def com_rev(message: types.Message):
    await message.answer(text='Введите строку')
    await Form.ans.set()


@dp.message_handler(state=Form.ans)
async def com_rev(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ans'] = message.text[::-1]
        await message.reply(text=data['ans'])
    await state.finish()


@dp.message_handler(commands=['capitalize'])
async def com_cap(message: types.Message):
    await message.answer(text='Введите строку')
    await Form.ans2.set()


@dp.message_handler(state=Form.ans2)
async def com_cap(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ans2'] = message.text.upper()
        await message.reply(text=data['ans2'])
    await state.finish()


@dp.message_handler(commands=['lower'])
async def com_low(message: types.Message):
    await message.answer(text='Введите строку')
    await Form.ans3.set()


@dp.message_handler(state=Form.ans3)
async def com_low(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ans3'] = message.text.lower()
        await message.reply(text=data['ans3'])
    await state.finish()


@dp.message_handler(commands=['random_letter'])
async def com_low(message: types.Message):
    await message.answer(text=random.choice(string.ascii_lowercase))


@dp.message_handler(commands=['random_number'])
async def com_low(message: types.Message):
    await message.answer(text=str(random.randrange(100) + 1))


@dp.message_handler()
async def smth(message: types.Message):
    await message.answer(text='Я такого не понимаю, напишите /help')


if __name__ == '__main__':
    executor.start_polling(dp)
