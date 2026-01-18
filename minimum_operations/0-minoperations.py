#!/usr/bin/python3
"""
Minimum Operations module
"""


def minOperations(n):
    """
    Calculate fewest operations to get n H characters
    """
    if n <= 1:
        return 0
    
    operations = 0
    factor = 2
    
    while factor * factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    
    if n > 1:
        operations += n
    
    return operations
