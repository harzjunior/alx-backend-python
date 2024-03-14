#!/usr/bin/env python3
'''Task 7's module.
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Converts a key & its val to a tuple of the key &
    the sqr of its val.
    '''
    return (k, float(v**2))
