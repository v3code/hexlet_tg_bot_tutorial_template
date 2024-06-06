import logging
from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery, User
from aiogram.fsm.context import FSMContext

from shop_bot.admin.fsm import ProductsFormFSM
from shop_bot.admin.views import admin_main_view
from shop_bot.shop.service import add_product


router = Router(name="admin")

@router.message(F.text == "Админка")
async def admin(message: Message):
    await message.answer("Админка", reply_markup=admin_main_view())

@router.callback_query(F.data == "add_product")
async def add_product_route(callback: CallbackQuery, state: FSMContext):
    await state.set_state(ProductsFormFSM.name)
    await callback.answer()
    match callback.message:
        case Message():
            await callback.message.answer("Напишите название товара")
        case _:
            logging.info("Something went wrong")


@router.message(ProductsFormFSM.name)
async def product_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(ProductsFormFSM.description)
    await message.answer("Напишите описание")

@router.message(ProductsFormFSM.description)
async def product_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await state.set_state(ProductsFormFSM.price)
    await message.answer("Напишите цену")

@router.message(ProductsFormFSM.price)
async def product_price(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    data = await state.get_data()
    await state.clear()
    user: User = message.from_user # type: ignore
    
    await add_product(
        name=data['name'],
        description=data['description'],
        price=float(data['price']),
        user_id=user.id
    )
    await message.answer("Товар добавлен")
    
