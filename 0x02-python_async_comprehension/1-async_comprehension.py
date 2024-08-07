#!/usr/bin/env python3
"""this module defines a coroutine"""
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list:
    """This fucntion will collect 0 random
    numbers using an async comprehensing over async_generator"""
    re_list = [i async for i in async_generator()]
    return re_list
