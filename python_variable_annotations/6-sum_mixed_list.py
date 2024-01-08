#!/usr/bin/env python3
""" type-annotated function list of floats """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """
    returns float
    """
    return sum(mxd_lst)
