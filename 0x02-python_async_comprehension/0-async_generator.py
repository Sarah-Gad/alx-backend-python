#!/usr/bin/env python3
"""This module defines an async  generator"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """This fucntion yields a random number between 0 and 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        ram_num = random.uniform(0, 10)
        yield ram_num
