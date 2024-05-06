class ShopBotError(Exception):

    def __init__(self, message: str) -> None:
        self.message = message
        
    def __repr__(self) -> str:
        return self.message
    

class InvalidUserError(ShopBotError):

    def __init__(self) -> None:
        super().__init__("Некорректный пользователь")
