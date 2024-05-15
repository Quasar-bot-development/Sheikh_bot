from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


subscription_keyboard = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="Подписаться", url="https://t.me/barrel_token"),
    InlineKeyboardButton(text="Проверить", callback_data="check_subscription"),
    ]]
)

main_keyboard = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="Баланс", callback_data="balance"),
    InlineKeyboardButton(text="Вывод", callback_data="withdraw"),
    InlineKeyboardButton(text="Пригласить", callback_data="invite_friend"),
    ]]
)
