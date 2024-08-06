#!/usr/bin/env python3
"""Function for basic async syntax"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0
    and max_delay seconds.

    Args:
        max_delay (int): Maximum delay in seconds (inclusive).

    Returns:
        float: The random delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
