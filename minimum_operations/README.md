Minimum Operations
Project Description

In this project, we start with a text file that contains only one character: H.

The text editor allows only two operations:

Copy All and Paste
Given a number n, the goal is to calculate the minimum number of operations needed to get exactly n characters H in the file.
If it is impossible to reach exactly n characters, the function should return 0.

Function Prototype: def minOperations(n): Returns an integer If n <= 1, returns 0 Example: n = 9

H → Copy All → Paste → HH → Paste → HHH → Copy All → Paste → HHHHHH → Paste → HHHHHHHHH

Number of operations: 6
