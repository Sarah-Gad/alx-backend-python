#!/usr/bin/env python3
"""This module return asyncio.task"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """This fucntion return asyncio.Task"""
    task1: asyncio.Task = asyncio.create_task(wait_random(max_delay))
    return task1
