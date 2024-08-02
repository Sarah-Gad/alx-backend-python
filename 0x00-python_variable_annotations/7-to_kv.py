#!/usr/bin/env python3
"""This module define some variables"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """This fucntion returns a tuple"""
    return (k, v**2)
