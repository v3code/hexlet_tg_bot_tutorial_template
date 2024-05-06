from shop_bot.errors import ShopBotError


class NoItemsForUpdatingProduct(ShopBotError):

    def __init__(self) -> None:
        super().__init__("Нужно, чтобы было хотя-бы одно значение, которое нужно изменить в товаре")


class ProductForEditionNotExists(ShopBotError):
    def __init__(self) -> None:
        super().__init__("Продукт для редактирования не существует")

 
class ProductNotExists(ShopBotError):
    def __init__(self) -> None:
        super().__init__("Продукт не существует")
