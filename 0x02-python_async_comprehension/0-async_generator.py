#!/usr/bin/env python3
'''a coroutine called async_generator that takes no arguments.'''


import asyncio
from typing import AsyncGenerator
import random


async def async_generator() -> AsyncGenerator[float, None]:
    '''Yields a random number between 0 and 10'''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
