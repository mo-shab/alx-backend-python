#!/usr/bin/env python3
"""Module for measure runtime"""


import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay),
    and returns the average time per call.

    Args:
        n (int): Number of times to call wait_random within wait_n.
        max_delay (int): Maximum delay for wait_random.

    Returns:
        float: Average time per call.
    """
    # Record the start time
    start_time = time.time()

    # Run the wait_n coroutine and wait for it to finish
    asyncio.run(wait_n(n, max_delay))

    # Record the end time
    end_time = time.time()

    # Calculate the total elapsed time
    total_time = end_time - start_time

    # Return the average time per call
    return total_time / n
