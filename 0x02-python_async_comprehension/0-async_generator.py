#!/usr/bin/env python3

""" import the asyncio and random module"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ a Async Generator

    Yield:
        random number between 0 and 10
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
