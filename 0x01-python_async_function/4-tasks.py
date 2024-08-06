#!/usr/bin/env python3
"""Task wait random"""


from typing import List

task_wait_random = __import__('3-task').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns task_wait_random n times with a specified max_delay.

    Args:
        n (int): Number of times to call task_wait_random.
        max_delay (int): Maximum delay for wait_random.

    Returns:
        List[float]: List of delays in ascending order.
    """
    # Create n tasks using task_wait_random
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    
    # Await all the tasks and collect their results
    delays = [await task for task in tasks]
    
    # Return the delays sorted in ascending order
    return sorted(delays)
