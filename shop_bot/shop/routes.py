import logging
from typing import Any, Dict
from aiogram import Bot, Router, F
from aiogram.filters import CommandStart, ExceptionTypeFilter
from aiogram.types import Message, User, ErrorEvent


from shop_bot.errors import InvalidUserError
from shop_bot.shop.views import main_menu_view


router = Router(name="shop")


@router.message(CommandStart())
async def start(message: Message, is_admin: bool):
    user: User = message.from_user # type: ignore
    await message.answer(f"Привет! {user.full_name}", reply_markup=main_menu_view(is_admin))
    


@router.message(F.photo)
async def answer_hello(message: Message):
    await message.reply("Its a photo")
    

@router.error()
async def handle_general_error(event: ErrorEvent, message: Message, is_admin: bool):
    logging.critical("Critical error caused by %s", event.exception, exc_info=True)
    await message.answer("Упс =(. Что-то пошло не так", reply_markup=main_menu_view(is_admin))
    

@router.error(ExceptionTypeFilter(InvalidUserError))
async def handle_invalid_user(event: ErrorEvent, message: Message):
    await message.answer(str(event.exception))
