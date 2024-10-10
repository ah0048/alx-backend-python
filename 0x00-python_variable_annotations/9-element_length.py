#!/usr/bin/env python3
'''Type-annotated element_length function'''


from typing import Sequence, Union, Any, List, Tuple


def element_length(lst: Sequence[Any]) -> List[Tuple[Any, int]]:
    '''Returns a list of the lengths of the elements in lst'''
    return [(i, len(i)) for i in lst]
