#!/usr/bin/env python3
"""This module define some variables"""
from typing import Sequence, List, Tuple


def element_length(lst: Sequence) -> List[Tuple[Sequence, int]]:
    """a function"""
    return [(i, len(i)) for i in lst]
