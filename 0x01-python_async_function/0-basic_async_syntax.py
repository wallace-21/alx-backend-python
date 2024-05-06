#!/usr/bin/ env python3

""" import the async and random module"""
import asyncio
import random


async def wait_random(max_delay: int = 10 ) -> float:
    """funcion that prints 3 randown which includes
       parameters:
             max_delay: int: delay around/random delay
       return:
           a random delay 
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return (delay)
