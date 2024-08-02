#!/usr/bin/env python3
"""This module define some variables"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """This fucntion takes a float multiplier as argument and returns a
    function that multiplies a float by multiplier."""
    def multi(f: float) -> float:
        """Thiis is the callable"""
        return f * multiplier

    return multi
