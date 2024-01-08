#!/usr/bin/env python3
"""asynchronous coroutine """
import random
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    returns list of delays in asc order """
    delays = []
    for x in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)
    sorted_delays = sorted(delays)
    return sorted_delays
