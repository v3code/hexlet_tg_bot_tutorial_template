from shop_bot.errors import ShopBotError


class UserAlreadyAdmin(ShopBotError):

    def __init__(self) -> None:
        super().__init__("Пользователь уже является админом")


class AdminRestrictionError(ShopBotError):

    def __init__(self) -> None:
        super().__init__("Доступно только для администраторов")


class UserAlreadyIsNotAdmin(ShopBotError):

    def __init__(self) -> None:
        super().__init__("Пользователь уже не является администратором")


class UserNeverBeenAdmin(ShopBotError):

    def __init__(self) -> None:
        super().__init__(
            "Данный пользователь никогда и не был администратором")
