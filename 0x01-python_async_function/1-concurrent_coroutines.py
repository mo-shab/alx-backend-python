#!/usr/bin/env python3
"""Function for concurrent coroutines"""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns wait_random n times with a 
    specified max_delay.

    Args:
        n (int): Number of times to call wait_random.
        max_delay (int): Maximum delay for wait_random.

    Returns:
        List[float]: List of delays in ascending order.
    """
    # List of asyncio.Task objects
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    # Await all the tasks and collect their results
    delays = [await task for task in tasks]

    # Return the delays sorted in ascending order
    return sorted(delays)
