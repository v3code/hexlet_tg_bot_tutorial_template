from decimal import Decimal
from typing import NamedTuple, Optional

from sqlalchemy import exists, func, select, update

from shop_bot.shop.errors import NoItemsForUpdatingProduct
from shop_bot.shop.models import Product
from shop_bot.utils import delete_none_from_dict


class ProductUpdateData(NamedTuple):
    name: Optional[str] = None
    price: Optional[Decimal] = None
    description: Optional[str] = None
    photo: Optional[str] = None


def update_product_by_id(id: int, update_data: ProductUpdateData):

    update_dict = delete_none_from_dict(update_data._asdict())
    if not update_dict:
        raise NoItemsForUpdatingProduct()

    return update(Product).where(Product.id == id,
                                 ~Product.archived).values(**update_dict)


def is_product_exists_by_id(id: int):
    return exists(Product).where(Product.id == id, ~Product.archived).select()


def get_product_by_id(id: int):
    return select(Product).where(Product.id == id, ~Product.archived)


def get_total_products():
    return select(func.count()).select_from(Product).where(~Product.archived)


def get_products_with_limit_and_offset(limit: int, offset: int):
    return select(Product.id, Product.name, Product.price).where(~Product.archived) \
        .offset(offset).limit(limit).order_by(Product.updated_at)
    
