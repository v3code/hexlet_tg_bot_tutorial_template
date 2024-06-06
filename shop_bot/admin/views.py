
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import KeyboardButton, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData


def admin_main_view():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Доавить товар", callback_data="add_product")

    return keyboard.as_markup() 
