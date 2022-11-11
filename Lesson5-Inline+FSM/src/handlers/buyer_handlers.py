from aiogram import types
from aiogram.types import ReplyKeyboardRemove, InputFile, InputMediaPhoto

from loader import dp, db, bot
from keyboards import commands_dafault_keyboard, see_commands_default_keyboard, info_default_keyboard


@dp.message_handler(text=['Привет', 'Начать'])
@dp.message_handler(commands='start')
async def answer_start_command(message: types.Message):
    await message.answer(text=f'Привет, {message.from_user.first_name}!'
                              f'\nРад тебя видеть!',
                              reply_markup=ReplyKeyboardRemove())
    await message.answer(text=f'{message.from_user.first_name}, напипши интересуюущую команду или введи Помощь для вывода списка команд:')


@dp.message_handler(text='Помощь')
@dp.message_handler(commands='help')
async def answer_help_command(message: types.Message):
    await message.answer(text=f'Список команд представлен на кливиатуре',
                              reply_markup=commands_dafault_keyboard)


@dp.message_handler(text=['Иформация о компании'])
@dp.message_handler(commands='info')
async def answer_info_command(message: types.Message):
    await message.answer(text=f'Информация представлена на клавиатуре',
                              reply_markup=info_default_keyboard)

@dp.message_handler(text=['График работы'])
async def answer_graph_command(message: types.Message):
    await message.answer(text=f'Мы работаем:'
                                f'\nПн-пт: с 11 до 19'
                                f'\nСб-вс: с 11 до 18',
                                reply_markup=info_default_keyboard)

@dp.message_handler(text=['Контакты'])
async def answer_contact_command(message: types.Message):
    await message.answer(text=f'Звоните в любое время: +79025556677',
                                reply_markup=info_default_keyboard)

@dp.message_handler(text=['В общее меню команд'])
async def answer_main_command(message: types.Message):
    await message.answer(text=f'Список команд представлен на кливиатуре:',
                                reply_markup=commands_dafault_keyboard)


@dp.message_handler(text='Скрыть')
@dp.message_handler(text=['Скрыть клавиатуру'])
async def answer_shadow_command(message: types.Message):
    await message.answer(text=f'Мы ее спрятали :)',
                                reply_markup=see_commands_default_keyboard)


@dp.message_handler(text='Показать')
@dp.message_handler(text=['Показать клавиатуру'])
async def answer_shadow_command(message: types.Message):
    await message.answer(text=f'Список команд представлен на кливиатуре:',
                                reply_markup=commands_dafault_keyboard)


@dp.message_handler(content_types=['contact'])
async def answer_contact_command(message: types.Message):
    if message.from_user.id == message.contact.user_id:
        await message.answer(text=f'Это твой контакт, зарегистрирован!')
        db.add_user(int(message.from_user.id), str(message.contact.phone_number))
    else:
        await message.answer(text=f'А это кто?')

# @dp.message_handler()
# async def answer_command(message: types.Message):
#     await message.answer(text=f'Я такого пока не знаю...')
