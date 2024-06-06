from aiogram.fsm.state import StatesGroup, State

class ProductsFormFSM(StatesGroup):
    name = State()
    description = State()
    price = State()