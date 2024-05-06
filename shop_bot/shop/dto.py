from dataclasses import dataclass
from decimal import Decimal
from typing import Iterable, List

from sqlalchemy import RowMapping


@dataclass(slots=True)
class ProductsListItem:
    id: int
    name: str
    price: Decimal

@dataclass(slots=True)
class ProductsPaginated:
    total_pages: int
    page: int
    products: List[ProductsListItem]
    
    @staticmethod
    def from_mapped_sequence(total_pages: int, page: int, products_rows: Iterable[RowMapping]):
        return ProductsPaginated(
            total_pages=total_pages,
            page=page,
            products=[ProductsListItem(**row) for row in products_rows]
        )
        