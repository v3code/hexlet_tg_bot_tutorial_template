from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import Message
from shop_bot.admin.errors import AdminRestrictionError
from shop_bot.admin.service import is_user_admin


class IsAdminMiddleware(BaseMiddleware):

    async def __call__(self, handler: Callable[[Message, Dict[str, Any]],
                                               Awaitable[Any]], event: Message,
                       data: Dict[str, Any]) -> Any:
        user_id: int = event.from_user.id  # type: ignore User always has id
        is_admin = await is_user_admin(user_id)
        data['is_admin'] = is_admin
        return await handler(event, data)


class AdminGuard(BaseMiddleware):

    async def __call__(self, handler: Callable[[Message, Dict[str, Any]],
                                               Awaitable[Any]], event: Message,
                       data: Dict[str, Any]) -> Any:
        if not data.get("is_admin", False):
            raise AdminRestrictionError()
        return await handler(event, data)
