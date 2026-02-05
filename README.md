# Rainwater Retention

This project implements a solution to calculate how much rainwater will be retained between walls of varying heights, represented as a list of non-negative integers.

---

## Task

0. Rain
Write a function rain(walls) that calculates the total amount of rainwater that will be retained between the walls after rainfall.

Prototype:

def rain(walls)
walls is a list of non-negative integers where each integer represents the height of a wall at that position.
The function should return an integer representing the total amount of rainwater retained between the walls.
If the list is empty, return 0.

Constraints
.The ends of the list (before index 0 and after index walls[-1]) do not retain water.
.The solution must handle multiple gaps and varying wall heights.

Example Usage
python
Copy code
walls = [0, 1, 0, 2, 0, 3, 0, 4]
print(rain(walls))  # 6

walls = [2, 0, 0, 4, 0, 0, 1, 0]
print(rain(walls))  # 6
Explanation
Water is trapped between taller walls.

At every index:

ini
Copy code
water = min(max_left, max_right) - current_height
We use the two-pointer technique to efficiently compute trapped water in O(n) time and O(1) space.

Dry Run Example
Walls:

csharp
Copy code
[0, 1, 0, 2, 0, 3, 0, 4]
Step-by-step calculation
Step	Left	Right	Height(L)	Height(R)	Left Max	Water Added	Total
1	0	7	0	4	0	0	0
2	1	7	1	4	1	0	0
3	2	7	0	4	1	1	1
4	3	7	2	4	2	0	1
5	4	7	0	4	2	2	3
6	5	7	3	4	3	0	3
7	6	7	0	4	3	3	6

Final trapped water = 6 units

Running the Program
To test the rain function, run the following command:

./0_main.py
The 0_main.py script imports the rain function and uses example inputs to demonstrate the functionality of the program.

Example Output:
6
6
Repository
GitHub repository: alu-interview
Directory: rain
File: 0-rain.py
6
6
