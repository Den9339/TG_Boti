from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

commands_dafault_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/start'),
            KeyboardButton(text='/item')
        ],
        [
            KeyboardButton(text=f'/help'),
            KeyboardButton(text='/info')
        ],
        [
            KeyboardButton(text=f'Поделиться контактом',
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
            KeyboardButton(text='О нас'),
            KeyboardButton(text='О боте')
        ],
        [
            KeyboardButton(text='В общее меню команд')
        ]
    ],
    resize_keyboard=True
)