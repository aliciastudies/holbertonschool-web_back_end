#!/usr/bin/env python3
""" type-annotated function functions """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns float
    """
    def function(input: float) -> float:
        return input * multiplier
    return (function)
