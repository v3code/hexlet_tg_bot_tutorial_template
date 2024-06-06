import logging
from aiogram import Bot, Dispatcher
from shop_bot.admin.middleware import IsAdminMiddleware
from shop_bot.shop.routes import router as shop_router


from shop_bot import config


async def start_bot():
    if config.IS_DEBUG:
        logging.basicConfig(level=logging.INFO)

    bot = Bot(token=config.TOKEN)
    dispatcher = Dispatcher()
    
    dispatcher.message.middleware(IsAdminMiddleware())

    dispatcher.include_routers(shop_router)

    await dispatcher.start_polling(bot)