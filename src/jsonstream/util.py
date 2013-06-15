#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2012 Nigel Small
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""" Utilities.
"""


def assembled(iterable):
    """ Assembles a JSON-derived value from a set of key-value pairs as
    produced by the JSONStream process in a similar way to the built-in `dict`
    function. Uses the `merged` function on each pair to build the return
    value.
    """
    obj = None
    for key, value in iterable:
        obj = merged(obj, key, value)
    return obj


def merged(obj, key, value):
    """ Merge value with object supplied at a position described by iterable
    key. The key describes a navigable path through the object hierarchy with
    integer items describing list indexes and other types of items describing
    dictionary keys.
    
        >>> obj = None
        >>> obj = merged(obj, ("drink",), "lemonade")
        >>> obj
        {'drink': 'lemonade'}
        >>> obj = merged(obj, ("cutlery", 0), "knife")
        >>> obj = merged(obj, ("cutlery", 1), "fork")
        >>> obj = merged(obj, ("cutlery", 2), "spoon")
        >>> obj
        {'cutlery': ['knife', 'fork', 'spoon'], 'drink': 'lemonade'}
        
    """
    if key:
        k = key[0]
        if isinstance(k, int):
            if isinstance(obj, list):
                obj = list(obj)
            else:
                obj = []
            while len(obj) <= k:
                obj.append(None)
        else:
            if isinstance(obj, dict):
                obj = dict(obj)
            else:
                obj = {}
            obj.setdefault(k, None)
        obj[k] = merged(obj[k], key[1:], value)
        return obj
    else:
        return value
