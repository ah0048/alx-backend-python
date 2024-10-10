#!/usr/bin/env python3
'''Type-annotated element_length function'''


from typing import Sequence, Union, Any, List, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Returns a list of the lengths of the elements in lst'''
    return [(i, len(i)) for i in lst]
