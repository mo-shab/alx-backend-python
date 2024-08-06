#!/usr/bin/env python3
"""Task wait random"""


import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task for the wait_random coroutine with a given max_delay.

    Args:
        max_delay (int): Maximum delay for wait_random.

    Returns:
        asyncio.Task: A task object representing the execution of wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
