#!/usr/bin/env python3
"""Asynchronous Generator"""

import asyncio
import random

async def async_generator():
    """Generate 10 random numbers between 0 and 10"""
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.uniform(0, 10)  # Yield a random number between 0 and 10
