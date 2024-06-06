import logging
from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery, User

from shop_bot.shop.views import CatalogCallback, catalog_view, main_menu_view


router = Router(name="shlop")

@router.message(CommandStart())
async def start(message: Message, is_admin: bool):
    user: User = message.from_user # type: ignore
    logging.info(user)
    await message.answer("Hello!", reply_markup=main_menu_view(is_admin))


@router.callback_query(CatalogCallback.filter(F.page > 0))
async def catalog(callback_query: CallbackQuery):
    match callback_query.message:
        case Message():
            await callback_query.message.answer("Catalog", reply_markup=catalog_view())
        case _:
            pass


    # await callback_query.message.answer("Catalog", reply_markup=catalog_view())


@router.message(F.text.contains("Hexlet"))
async def contains_hexlet(message: Message):
    await message.reply("hexlet in message")