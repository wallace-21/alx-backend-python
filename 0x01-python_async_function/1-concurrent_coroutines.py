#!/usr/bin/env python3

""" import async module and a function wait_random"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> float:
    """
    function that returns a list of floats

    Parameters:
        n (int): number of values

        max_delay (int): The maximum delay

    Returns:
        List[float]: a list of floats
    """
    delays = []
    for i in range(n):
        delay = await wait_random(max_delay)
        j = len(delays)
        while j > 0 and delays[j - 1] > delay:
            j -= 1
        delays.insert(j, delay)

    return delays
