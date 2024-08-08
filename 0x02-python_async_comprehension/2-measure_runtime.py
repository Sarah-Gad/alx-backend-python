#!/usr/bin/env python3
"""This module f=defines a coreoutine"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """This function will execute async_comprehension four times
    in parallel and  measure the total runtime and return it."""
    start_time = time.time()
    list_tasks = []
    for _ in range(4):
        list_tasks.append(asyncio.create_task(async_comprehension()))
    await asyncio.gather(*list_tasks)
    return time.time() - start_time
