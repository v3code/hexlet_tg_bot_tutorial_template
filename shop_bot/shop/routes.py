import logging
from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery, User

from shop_bot.admin import routes
from shop_bot.shop.service import get_products_paginated
from shop_bot.shop.views import CatalogCallback, catalog_view, main_menu_view, catalog_main_view


router = Router(name="shop")

@router.message(CommandStart())
async def start(message: Message, is_admin: bool):
    user: User = message.from_user # type: ignore
    logging.info(user)
    await message.answer("Hello!", reply_markup=main_menu_view(is_admin))

@router.message(F.text == "Каталог")
async def main_menu_catalog(message: Message):
    await message.answer("Чтобы посмотреть каталог, нажмите на кнопку", reply_markup=catalog_main_view())


@router.callback_query(CatalogCallback.filter())
async def catalog(callback: CallbackQuery, callback_data: CatalogCallback):
    products_data = await get_products_paginated(page=callback_data.page, 
                                                 limit=callback_data.limit)
    await callback.answer()
    match callback.message:
        case Message():
            await callback.message.edit_text(f"Выберете товар, страница {callback_data.page}", 
                                             reply_markup=catalog_view(callback_data, products_data))
        case _:
            logging.info("No message in callback")


# @router.callback_query(CatalogCallback.filter())
# async def handle_catalog(callback: CallbackQuery, callback_data: CatalogCallback):
#     await callback.answer("Catalog", show_alert=True)
    # match callback.message:
    #     case Message():
    #         await callback.message.answer("Catalog", reply_markup=catalog_view())
    #     case _:
    #         logging.info("Something went wrong")


    # await callback_query.message.answer("Catalog", reply_markup=catalog_view())
