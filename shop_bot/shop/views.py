from re import T
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import KeyboardButton, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData


class CatalogCallback(CallbackData, prefix="catalog"):
    page: int = 1
    limit: int = 5

def main_menu_view(is_admin: bool = False):
    keyboard = ReplyKeyboardBuilder()
    keyboard.add(KeyboardButton(text="Каталог", callback_data=CatalogCallback().pack()))
    keyboard.add(KeyboardButton(text="Корзина"))
    keyboard.add(KeyboardButton(text="Мои заказы"))
    keyboard.add(KeyboardButton(text="Hexlet", url="https://hexlet.io/"))
    if is_admin:
        keyboard.add(KeyboardButton(text="Админка"))
    
    keyboard.adjust(1, 3, 1)

    return keyboard.as_markup(resize_keyboard=True)

products = [
    {"id": 1, "name": "Товар 1", "price": 100.00},
    {"id": 2, "name": "Товар 2", "price": 200.00},
    {"id": 3, "name": "Товар 3", "price": 300.00},
    {"id": 4, "name": "Товар 4", "price": 400.00},

]


def catalog_view():
    keyboard = InlineKeyboardBuilder()
    for product in products:
        text = f"{product['name']}, цена: {product['price']}"
        keyboard.add(InlineKeyboardButton(text=text))
    
    keyboard.add(InlineKeyboardButton(text="Назад"))
    keyboard.add(InlineKeyboardButton(text="Вперед"))
    keyboard.add(InlineKeyboardButton(text="Ко"))
    
    return keyboard.as_markup()
    
