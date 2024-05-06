from datetime import datetime
from decimal import Decimal
from typing import List

from sqlalchemy import Column, ForeignKey, Numeric, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from shop_bot.base_model import BaseModel


orders_to_products_table = Table(
    "orders_to_products",
    BaseModel.metadata,
    Column("order_id", ForeignKey("orders.id"), primary_key=True),
    Column("product_id", ForeignKey("products.id"), primary_key=True),
)


class Product(BaseModel):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[Decimal] = mapped_column(Numeric(10, 4))
    photo: Mapped[str] = mapped_column(nullable=True)

    added_by_user: Mapped[int]

    archived: Mapped[bool] = mapped_column(default=False)

    created_at: Mapped[datetime] = mapped_column(default=func.now())
    updated_at: Mapped[datetime] = mapped_column(default=func.now(),
                                                 onupdate=func.now())
    


# class Cart(BaseModel):
#     __tablename__ = "cart" 
#     user_id: Mapped[int] = mapped_column(primary_key=True)
#     user: Mapped[int] = relationship()


class Order(BaseModel):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int]
    products: Mapped[List[Product]] = relationship(secondary=orders_to_products_table)
    
    total_price: Mapped[Decimal] = mapped_column(Numeric(10, 4))
    created_at: Mapped[datetime] = mapped_column(default=func.now())
