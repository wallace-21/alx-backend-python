#!/usr/bin/env python3

"""import the asyncio and random"""
import asyncio
import random
from typing import Generator

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator:
    """Coroutine to collect 10 random numbers using async comprehension.

    Returns:
        List of 10 random numbers.
    """
    result: Generator[float, None, None]= [i async for i in async_generator()]
    return result
