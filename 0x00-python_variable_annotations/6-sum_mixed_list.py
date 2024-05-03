#!/usr/bin/env python3

"""import a module called typing"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """ accepts a list that has integers and floats"""
    total = 0.0
    for numbers in mxd_lst:
        total += numbers

    return (total)
