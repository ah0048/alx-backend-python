#!/usr/bin/env python3
'''The basics of async syntax'''


import asyncio
import random
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Measure the runtime of wait_n'''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    return (end_time - start_time) / n
