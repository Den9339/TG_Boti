from loader import dp
from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from keyboards import commands_dafault_keyboard, see_commands_default_keyboard, info_default_keyboard

@dp.message_handler(text=['Привет', 'Начать'])
@dp.message_handler(commands='start')
async def answer_start_command(message: types.Message):
    await message.answer(text=f'Привет, {message.from_user.first_name}!'
                              f'\nРад тебя видеть!',
                                reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text='Добавить')
@dp.message_handler(commands='add')
async def answer_add_command(message: types.Message):
    await message.answer(text=f'Что добавить?',
                                reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text=['Ассортимент'])
@dp.message_handler(commands='item')
async def answer_add_command(message: types.Message):
    await message.answer(text=f'У нас в наличии:'
                              f'\n - редис'
                              f'\n - помидоры'
                              f'\n - капуста',
                              reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text='Показать')
@dp.message_handler(commands='help')
async def answer_add_command(message: types.Message):
    await message.answer(text=f'Список команд представлен на кливиатуре',
                              reply_markup=commands_dafault_keyboard)
    # await message.answer(text=f'/start - начать взаимодейсвие с ботом'
    #                           f'\n/item - ассортимент'
    #                           f'\n/add - добавить'
    #                           f'\n/help - помощь')

@dp.message_handler(text=['Иформация','Инфо', 'О'])
@dp.message_handler(commands='info')
async def answer_add_command(message: types.Message):
    await message.answer(text=f'Информация представлена на клавиатуре',
                              reply_markup=info_default_keyboard)

@dp.message_handler(text=['График работы'])
async def answer_add_command(message: types.Message):
    await message.answer(text=f'Мы работаем:'
                                f'\nПн-пт: с 11 до 19'
                                f'\nСб-вс: с 11 до 18',
                                reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text=['Контакты'])
async def answer_add_command(message: types.Message):
    await message.answer(text=f'Звоните в любое время: +79025556677',
                                reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text=['О нас'])
async def answer_add_command(message: types.Message):
    await message.answer(text=f'Перспективная развивающаяся молодая компания!',
                                reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text=['О боте'])
async def answer_add_command(message: types.Message):
    await message.answer(text=f'Перспективный развивающийся молодой бот!',
                                reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text=['В общее меню команд'])
async def answer_add_command(message: types.Message):
    await message.answer(text=f'Список команд представлен на кливиатуре',
                                reply_markup=commands_dafault_keyboard)


@dp.message_handler(text='Скрыть')
@dp.message_handler(text=['Скрыть клавиатуру'])
async def answer_start_command(message: types.Message):
    await message.answer(text=f'Мы ее спрятали :)',
                                reply_markup=see_commands_default_keyboard)  

@dp.message_handler(content_types=['contact'])
async def answer_start_command(message: types.Message):
    print(message)
    if message.from_user.id == message.contact.user_id:
        await message.answer(text=f'Это твой контакт')
    else:
        await message.answer(text=f'А это кто?')

@dp.message_handler()
async def answer_start_command(message: types.Message):
    await message.answer(text=f'Я такого пока не знаю...')
