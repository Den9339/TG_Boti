from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = '5720420228:AAGB4kD9CbQYufUvVKdxpVcZEYr6rLy5rm8'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(text=['Привет', 'Начать'])
@dp.message_handler(commands='start')
async def answer_start_command(message: types.Message):
    await message.answer(text=f'Привет!'
                              f'\nРад тебя видеть!')

@dp.message_handler(text=['Редис', 'Помидоры'])
@dp.message_handler(commands='add')
async def answer_add_command(message: types.Message):
    await message.answer(text=f'Что добавить?')

@dp.message_handler(commands='item')
async def answer_add_command(message: types.Message):
    await message.answer(text=f'Что еще за Item?')

@dp.message_handler(commands='help')
async def answer_add_command(message: types.Message):
    await message.answer(text=f'В чем тебе help?')

@dp.message_handler(text='Капуста')
async def answer_add_command(message: types.Message):
    await message.answer(text=f'С чем желаете капусту?')


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)