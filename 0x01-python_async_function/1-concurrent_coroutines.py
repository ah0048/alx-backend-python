#!/usr/bin/env python3
'''The basics of async syntax'''


import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List:
    '''spawn wait_random n times with the specified max_delay.'''
    coroutines = [wait_random(max_delay) for i in range(n)]
    delays = await asyncio.gather(*coroutines)
    return sorted(delays)
