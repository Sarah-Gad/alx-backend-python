#!/usr/bin/env python3
"""This module defines a coroutine"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """This fucntion returns total_time / n"""
    start: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end: float = time.time()
    gap: float = end - start
    return gap / n
