#!/usr/bin/env python3
""" type-annotated function iterables """
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    returns tuple
    """
    return [(i, len(i)) for i in lst]
