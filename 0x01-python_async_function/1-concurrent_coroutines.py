#!/usr/bin/env python3
'''The basics of async syntax'''


import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay) -> List:
    '''spawn wait_random n times with the specified max_delay.'''
    req_list = [await wait_random(max_delay) for i in range(n)]
    n = len(req_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if req_list[j] > req_list[j + 1]:
                req_list[j], req_list[j + 1] = req_list[j + 1], req_list[j]
    return req_list
