#!/usr/bin/env python3
'''The basics of async syntax'''


import asyncio
import random
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int = 0, max_delay: int = 10) -> float:
    '''Measure the runtime of wait_n'''
    start = asyncio.get_event_loop().time()
    asyncio.run(wait_n(n, max_delay))
    end = asyncio.get_event_loop().time()
    return (end - start) / n
