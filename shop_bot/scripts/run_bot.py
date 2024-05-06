#!/usr/bin/env python
import asyncio

from shop_bot.main import start_bot


def main():
    asyncio.run(start_bot())


if __name__ == "__main__":
    main()
