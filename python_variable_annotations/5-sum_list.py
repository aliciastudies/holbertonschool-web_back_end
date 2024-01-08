#!/usr/bin/env python3
""" type-annotated function list of floats """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    returns float
    """
    return sum(input_list)
