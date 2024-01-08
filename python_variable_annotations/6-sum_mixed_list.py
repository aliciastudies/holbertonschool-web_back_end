#!/usr/bin/env python3
""" type-annotated function list of mixed """
from typing import List, Union, Optional


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    returns float
    """
    return sum(mxd_lst)
