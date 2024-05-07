#!/usr/bin/env python3

""" import async module and a function wait_random"""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    function that returns a list of floats

    Parameters:
        n (int): number of values

        max_delay (int): The maximum delay

    Returns:
        List[float]: a list of floats
    """
    lists = []
    for i in range(n):
        lists.append(wait_random(max_delay))
    delays = []
    for j in asyncio.as_completed(lists):
        delays.append(await j)
    return (delays)
