from email import message
from itertools import count
from loader import dp, db, bot
from aiogram import types
from aiogram.types import ReplyKeyboardRemove, InputFile, InputMediaPhoto
from keyboards import commands_dafault_keyboard, see_commands_default_keyboard, info_default_keyboard
from keyboards import navigation_items_callback, get_item_inline_keyboard


@dp.message_handler(text=['Привет', 'Начать'])
@dp.message_handler(commands='start')
async def answer_start_command(message: types.Message):
    await message.answer(text=f'Привет, {message.from_user.first_name}!'
                              f'\nРад тебя видеть!')

@dp.message_handler(text='Добавить')
@dp.message_handler(commands='add')
async def answer_add_command(message: types.Message):
    await message.answer(text=f'Что добавить?',
                                reply_markup=ReplyKeyboardRemove())
    # db.add_item(int(2), str('Кабак123'), int(message.from_user.id))
    # db.add_item(int(message.from_user.id), str(message.contact.phone_number))

@dp.message_handler(text=['Ассортимент'])
@dp.message_handler(commands='item')
async def answer_item_command(message: types.Message):
    first_item_info = db.select_item(id = 1)
    first_item_info = first_item_info[0]
    _, name, quantity, photo_path = first_item_info
    item_text = f'Название товара: {name}'\
                f'\nКоличество товара: {quantity}'
    photo = InputFile(path_or_bytesio= photo_path)
    await message.answer_photo(photo = photo,
                               caption = item_text,
                               reply_markup=get_item_inline_keyboard)


@dp.callback_query_handler(navigation_items_callback.filter(for_data='items'))
async def see_new_item(call: types.CallbackQuery):
    print(call.data)
    current_item_id = int(call.data.split(':')[-1])
    first_item_info = db.select_item(id=current_item_id)
    first_item_info = first_item_info[0]
    _, name, quantity, photo_path = first_item_info
    item_text = f'Название товара: {name}'\
                f'\nКоличество товара: {quantity}'
    photo = InputFile(path_or_bytesio=photo_path)
    await bot.edit_message_media(media=InputMediaPhoto(media=photo,
                                                       caption=item_text),
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=get_item_inline_keyboard(id=current_item_id))



@dp.message_handler(text='Показать')
@dp.message_handler(commands='help')
async def answer_help_command(message: types.Message):
    await message.answer(text=f'Список команд представлен на кливиатуре',
                              reply_markup=commands_dafault_keyboard)
    # await message.answer(text=f'/start - начать взаимодейсвие с ботом'
    #                           f'\n/item - ассортимент'
    #                           f'\n/add - добавить'
    #                           f'\n/help - помощь')

@dp.message_handler(text=['Иформация','Инфо', 'О'])
@dp.message_handler(commands='info')
async def answer_info_command(message: types.Message):
    await message.answer(text=f'Информация представлена на клавиатуре',
                              reply_markup=info_default_keyboard)

@dp.message_handler(text=['График работы'])
async def answer_graph_command(message: types.Message):
    await message.answer(text=f'Мы работаем:'
                                f'\nПн-пт: с 11 до 19'
                                f'\nСб-вс: с 11 до 18',
                                reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text=['Контакты'])
async def answer_contact_command(message: types.Message):
    await message.answer(text=f'Звоните в любое время: +79025556677',
                                reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text=['О нас'])
async def answer_o_command(message: types.Message):
    await message.answer(text=f'Перспективная развивающаяся молодая компания!',
                                reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text=['О боте'])
async def answer_ob_command(message: types.Message):
    await message.answer(text=f'Перспективный развивающийся молодой бот!',
                                reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text=['В общее меню команд'])
async def answer_main_command(message: types.Message):
    await message.answer(text=f'Список команд представлен на кливиатуре',
                                reply_markup=commands_dafault_keyboard)


@dp.message_handler(text='Скрыть')
@dp.message_handler(text=['Скрыть клавиатуру'])
async def answer_shadow_command(message: types.Message):
    await message.answer(text=f'Мы ее спрятали :)',
                                reply_markup=see_commands_default_keyboard)  

@dp.message_handler(content_types=['contact'])
async def answer_contact_command(message: types.Message):
    # print(message)
    if message.from_user.id == message.contact.user_id:
        await message.answer(text=f'Это твой контакт, зарегистрирован!')
        db.add_user(int(message.from_user.id), str(message.contact.phone_number))
    else:
        await message.answer(text=f'А это кто?')

@dp.message_handler()
async def answer_command(message: types.Message):
    await message.answer(text=f'Я такого пока не знаю...')
