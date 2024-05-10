#!/usr/bin/env python3

import time
from asyncio import run
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average execution time for wait_n(n, max_delay).

    Parameters:
        n (int): Number of values.
        max_delay (int): The maximum delay.

    Returns:
        float: Average execution time per iteration.
    """
    start_time = time.time()
    run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return (total_time / n)
