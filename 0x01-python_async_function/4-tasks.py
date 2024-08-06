#!/usr/bin/env python3
"""This module defines a coreotine"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Thif function spawn wait_random n times with the specified max_delay."""
    list_tasks: List = []
    for _ in range(0, n):
        list_tasks.append(task_wait_random(max_delay))
    results: List[float] = await asyncio.gather(*list_tasks)
    results_sorted: List[float] = sorted(results)
    return results_sorted
