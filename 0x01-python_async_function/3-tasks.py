#!/usr/bin/env python3

""" import the asyncio module"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> None:
    task = asyncio.Task(wait_random(max_delay))

    return(task)
