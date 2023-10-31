#!/usr/bin/python3a

def islower(c):
    n = 97
    while n < 123:
        if ord(c) == n:
            return True
        n += 1
    return False
