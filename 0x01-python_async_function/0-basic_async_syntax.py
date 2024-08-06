#!/usr/bin/env python3
"""Thsi module defines an asynchronous coroutine """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """This coroutine waits for a random delay between 0 and max_delay"""
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
