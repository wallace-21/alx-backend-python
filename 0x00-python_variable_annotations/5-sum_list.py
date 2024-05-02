#!/usr/bin/env python3

""" import a module called typing"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """function that takes a single parameter
    and returns the sum of the list"""
    total = 0.00
    for numbers in input_list:
        total += numbers
    return (total)
