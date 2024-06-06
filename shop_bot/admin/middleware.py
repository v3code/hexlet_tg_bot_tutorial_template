from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import Message, User

from shop_bot.admin.service import is_user_admin

class IsAdminMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        user: User = event.from_user # type: ignore
        is_admin = await is_user_admin(user.id)
        data['is_admin'] = is_admin
        return await handler(event, data)