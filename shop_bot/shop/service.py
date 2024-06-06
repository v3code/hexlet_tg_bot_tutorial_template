from decimal import Decimal
import logging
from typing import Optional

from shop_bot.db import async_session
from shop_bot.shop.dto import ProductsPaginated
from shop_bot.shop.errors import ProductForEditionNotExists, ProductNotExists
from shop_bot.shop.models import Product
from shop_bot.shop.repo import (ProductUpdateData, is_product_exists_by_id,
                                update_product_by_id, get_total_products,
                                get_products_with_limit_and_offset,
                                get_product_by_id)
from shop_bot.utils import get_offset_from_page, get_total_pages


async def add_product(name: str,
                      description: str,
                      price: float,
                      user_id: int,
                      photo: Optional[str] = None):
    dec_price = Decimal.from_float(price)
    product = Product(name=name,
                      description=description,
                      photo=photo,
                      added_by_user=user_id,
                      price=dec_price)
    async with async_session() as session:
        session.add(product)
        await session.commit()


async def is_product_exists(id: int):
    async with async_session() as session:
        result = await session.execute(is_product_exists_by_id(id))
        return result.scalar()  # type: ignore


async def edit_product(id: int,
                       name: Optional[str] = None,
                       description: Optional[str] = None,
                       price: Optional[float] = None,
                       photo: Optional[str] = None):

    if not await is_product_exists(id):
        raise ProductForEditionNotExists()

    processed_price = Decimal.from_float(price) if price is not None else None

    update_data = ProductUpdateData(name, processed_price, description, photo)

    async with async_session() as session:
        await session.execute(update_product_by_id(id, update_data))


async def get_total_product_count():
    async with async_session() as session:
        result = await session.execute(get_total_products())
        return result.scalar_one()


async def get_products_paginated(page: int = 1, limit: int = 5):
    products_count = await get_total_product_count()
    total_pages = get_total_pages(limit, products_count)
    if page < 1:
        page = 1
    if page > total_pages:
        page = total_pages
    offset = get_offset_from_page(page, limit)
    logging.info(offset)
    async with async_session() as session:
        result = await session.execute(
            get_products_with_limit_and_offset(limit, offset))
        products = result.mappings().all()
        return ProductsPaginated.from_mapped_sequence(total_pages=total_pages,
                                                      page=page,
                                                      products_rows=products)


async def get_product(id: int):
    async with async_session() as session:
        result = await session.execute(get_product_by_id(id))
        product = result.scalar_one_or_none()
        if product is None:
            raise ProductNotExists()
        
        return product
        
