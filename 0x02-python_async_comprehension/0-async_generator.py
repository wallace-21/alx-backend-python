#!/usr/bin/env python3

""" import the asyncio and random module"""

import asyncio
import random


async def async_generator() -> float:
    """ a Async Generator

    Yield:
        random number between 0 and 10
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.choice(range(0, 10))
