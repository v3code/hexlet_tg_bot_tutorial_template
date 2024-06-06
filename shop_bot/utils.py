import math
from typing import Any, Dict


def delete_none_from_dict(dct: Dict[Any, Any]):
    new_dct = {}
    for k, v in dct.items():
        if v is not None:
            new_dct[k] = v
    return new_dct


def get_total_pages(limit: int, total_entries: int):
    return int(math.ceil(total_entries / limit))


def get_offset_from_page(page: int, limit: int):
    return (page - 1) * limit
