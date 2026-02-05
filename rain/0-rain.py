#!/usr/bin/python3
"""Rain water trapping algorithm"""


def rain(walls):
    """Calculate trapped rainwater between walls
    
    Args:
        walls: List of non-negative integers representing wall heights
        
    Returns:
        Integer indicating total amount of rainwater retained
    """
    if not walls or len(walls) < 3:
        return 0
    
    left, right = 0, len(walls) - 1
    left_max, right_max = walls[left], walls[right]
    water = 0
    
    while left < right:
        if walls[left] < walls[right]:
            left += 1
            left_max = max(left_max, walls[left])
            water += left_max - walls[left]
        else:
            right -= 1
            right_max = max(right_max, walls[right])
            water += right_max - walls[right]
    
    return water

