#!/usr/bin/env python3
""" asynchronous coroutine """
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    returns float a random number between 0 and 10
    """
    for x in range(10):
        await asyncio.sleep(1)
        number = random.uniform(0, 10)
        yield number
