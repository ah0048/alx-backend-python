#!/usr/bin/env python3
'''Type-annotated to_kv function'''


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Returns a tuple containing the key and the square of the value'''
    return (k, v * v)
