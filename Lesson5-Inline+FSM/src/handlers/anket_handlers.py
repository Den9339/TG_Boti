from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message

from loader import dp, db, bot
from states import BuyerState
from keyboards import anket_callback, anket_keyboard, commands_dafault_keyboard


@dp.message_handler(text='Анкетирование')
async def show_anket(message: Message):
    await message.answer(text = 'Желаете заполнить небольшую анкету?',
                        reply_markup=anket_keyboard)


@dp.callback_query_handler(anket_callback.filter(action_anket='del_anket'))
async def del_anket(call: CallbackQuery):
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await bot.answer_callback_query(callback_query_id=call.id,
                                    text='Окей, продолжайте пользоваться ботом!',
                                    show_alert=True)


@dp.callback_query_handler(anket_callback.filter(action_anket='fill_anket'))
async def start_fill(call:CallbackQuery):
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await call.message.answer(text='Как оцениваете список товаров:')
    await BuyerState.wait_date.set()

@dp.message_handler(state=BuyerState.wait_date)
async def get_spisok(message: Message, state: FSMContext):
    await state.update_data({'spisok': message.text})
    await message.answer(text='Как оцениваете количество товара:')
    await BuyerState.wait_date.set()

@dp.message_handler(state=BuyerState.wait_date)
async def get_quantity(message: Message, state: FSMContext):
    await state.update_data({'quantity': message.text})
    await message.answer(text='Как оцениваете интерфейс бота, от 1 до 5:')
    await BuyerState.wait_date.set()

@dp.message_handler(state=BuyerState.wait_date)
async def get_inteface(message: Message, state: FSMContext):
    await state.update_data({'interface': message.text})
    await message.answer(text='Ваше пожелание:')
    await BuyerState.wait_date.set()

@dp.message_handler(state=BuyerState.wait_date)
async def get_pojelaniye(message: Message, state: FSMContext):
    await state.update_data({'pojelaniye': message.text})
    data = await state.get_data()
    text=f'Анкетирование' \
         f'\nКак оцениваете список товаров: {data["spisok"]}' \
         f'\nКак оцениватете количество товара: {data["quantity"]}' \
         f'\nКак оцениватете интерфейс бота: {data["interface"]}' \
         f'\nВаше пожелание: {data["pojelaniye"]}' \
    # await message.answer(text=text,
    #                     reply_markup=commands_dafault_keyboard)
    await state.reset_state()