# Rain Water Trapping

## Problem Description
Given a list of non-negative integers representing the heights of walls with unit width 1, calculate how many square units of water will be retained after it rains.

## Algorithm
Uses a two-pointer approach with O(n) time complexity and O(1) space complexity.

### Approach:
1. Use two pointers (left and right) starting from both ends
2. Track the maximum height seen from left and right
3. Move the pointer with smaller height inward
4. Calculate trapped water as the difference between max height and current height

### Time Complexity: O(n)
### Space Complexity: O(1)

## Usage
```python
rain = __import__('0-rain').rain

walls = [0, 1, 0, 2, 0, 3, 0, 4]
print(rain(walls))  # Output: 6

walls = [2, 0, 0, 4, 0, 0, 1, 0]
print(rain(walls))  # Output: 6
```

## Test
```bash
./0_main.py
```

Expected output:
```
6
6
```

