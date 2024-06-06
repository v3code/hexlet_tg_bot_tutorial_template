import logging
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import KeyboardButton, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData

from shop_bot.shop.dto import ProductsPaginated


class CatalogCallback(CallbackData, prefix="catalog"):
    page: int = 1
    limit: int = 5

def main_menu_view(is_admin: bool = False):
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text="Каталог")
    keyboard.button(text="Корзина")
    keyboard.add(KeyboardButton(text="Мои заказы"))
    keyboard.add(KeyboardButton(text="Hexlet"))
    if is_admin:
        keyboard.add(KeyboardButton(text="Админка"))
    
    keyboard.adjust(1, 3, 1)

    return keyboard.as_markup(resize_keyboard=True)


def catalog_main_view():
    keyboard = InlineKeyboardBuilder()
    logging.info(CatalogCallback().pack())
    keyboard.add(InlineKeyboardButton(text="Посмотреть каталог", callback_data=CatalogCallback().pack()))
    return keyboard.as_markup()

products = [
    {"id": 1, "name": "Товар 1", "price": 100.00},
    {"id": 2, "name": "Товар 2", "price": 200.00},
    {"id": 3, "name": "Товар 3", "price": 300.00},
    {"id": 4, "name": "Товар 4", "price": 400.00},
]


def catalog_view(catalog_pagination: CatalogCallback, products_data: ProductsPaginated):
    keyboard = InlineKeyboardBuilder()
    for product in products_data.products:
        text = f"{product.name}, цена: {product.price}"
        keyboard.add(InlineKeyboardButton(text=text, callback_data="product"))
    

    keyboard.add(InlineKeyboardButton(text="Корзина", callback_data="cart"))

    if catalog_pagination.page > 1:
        keyboard.add(InlineKeyboardButton(text="Назад",
                                          callback_data=CatalogCallback(page=catalog_pagination.page - 1).pack()))
    if catalog_pagination.page < products_data.total_pages:
        keyboard.add(InlineKeyboardButton(text="Вперед", 
                                          callback_data=CatalogCallback(page=catalog_pagination.page + 1).pack()))
    sizes = [1 for _ in range(len(products_data.products))]
    keyboard.adjust(*sizes, 1, 2)
    
    return keyboard.as_markup()
    
