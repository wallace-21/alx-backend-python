#!/usr/bin/ env python3

""" import the async and random module"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random delay before returning.

    Parameters:
        max_delay (int): The maximum delay in seconds. Default is 10.

    Returns:
        float: A random delay between 0 and max_delay seconds.
    """

    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return (delay)
