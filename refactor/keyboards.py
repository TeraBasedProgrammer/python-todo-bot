from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

answear_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) \
    .add(KeyboardButton('Да'), KeyboardButton('Нет'))

lists_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

help_keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton("Принцип работы бота"),
                                           InlineKeyboardButton("Список команд"))
help_undo_keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton("Назад"))
