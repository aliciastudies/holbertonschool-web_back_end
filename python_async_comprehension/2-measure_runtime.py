#!/usr/bin/env python3
""" asynchronous coroutine """
import asyncio
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    executes four times in parrallel
    """
    start_time = perf_counter()
    coroutines = [async_comprehension() for _ in range(4)]

    await asyncio.gather(*coroutines)

    end_time = perf_counter()
    total_runtime = end_time - start_time

    return total_runtime
