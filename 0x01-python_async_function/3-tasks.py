#!/usr/bin/env python3

""" import the asyncio module"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> None:
    """
    Create an asyncio.Task to execute the
    wait_random coroutine asynchronously.

    Parameters:
        max_delay (int): The maximum delay for
        the wait_random coroutine.

    Returns:
        asyncio.Task: A Task object representing
        the execution of wait_random coroutine.
    """
    task = asyncio.Task(wait_random(max_delay))

    return(task)
