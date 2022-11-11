from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

commands_dafault_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f'Список товаров'),
            KeyboardButton(text=f'Корзина')
        ],
        [
            KeyboardButton(text=f'Помощь'),
            KeyboardButton(text=f'Иформация о компании')
        ],
        [
            KeyboardButton(text=f'Активация аккаунта',
                                request_contact=True),
            KeyboardButton(text=f'Поделиться геолокацией',
                                request_location=True)
        ],
        [
            KeyboardButton(text=f'Скрыть клавиатуру')  
        ]
    ], 
    resize_keyboard=True
)

see_commands_default_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Показать')
        ]
    ],
    resize_keyboard=True
)

info_default_keyboard = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='График работы'),
            KeyboardButton(text='Контакты')
        ],
        [
            KeyboardButton(text='В общее меню команд')
        ]
    ],
    resize_keyboard=True
)