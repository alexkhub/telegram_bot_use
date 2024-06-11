from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

help_keyboard = ReplyKeyboardMarkup(resize_keybord=True, keyboard=[
    [
        KeyboardButton(
            text='/register'

        ),

    ],
    [
        KeyboardButton(
            text='/view_scores'
        )
    ],
    [
        KeyboardButton(
            text='/enter_scores'
        )
    ]

]
)