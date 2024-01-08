#!/usr/bin/env python3
"""asynchronous coroutine """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    returns random delay between 0 and max_delay
    """
    delay = max_delay * random.random()
    await asyncio.sleep(delay)
    return delay
