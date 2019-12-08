# Copyright 2019 Jake Waffle. Subject to the Apache2 license.

def contains_key(key):
    return lambda fields: 1 if key in fields else 0

def contains_field(key, value):
    return lambda fields: 1 if key in fields and fields[key] == value else 0
