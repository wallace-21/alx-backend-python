#!/usr/bin/env python3

"""function that returns a list"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ it acceepts a single list"""
    return [(i, len(i)) for i in lst]
