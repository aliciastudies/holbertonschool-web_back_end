#!/usr/bin/env python3
"""asyncronous coroutine task_wait_n """
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    returns the list of delays in asc order
    """
    delays = []
    for x in range(n):
        delay = await task_wait_random(max_delay)
        delays.append(delay)
    sorted_delays = sorted(delays)
    return sorted_delays
