#!/usr/bin/env python3
"""This module define a method"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """a method that will Retrieves
    the first element of a sequence"""
    if lst:
        return lst[0]
    else:
        return None
