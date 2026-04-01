Pascal's Triangle
Description

This project contains a Python implementation of a function that generates Pascal's Triangle.

Pascal's Triangle is a triangular array of binomial coefficients that appears in probability theory, combinatorics, and algebra. Each number is the sum of the two numbers directly above it.

 Function Specification
pascal_triangle(n)

This function:

Takes an integer n as input
Returns a list of lists of integers representing Pascal’s Triangle up to the nth row
Returns an empty list [] if n <= 0
Usage

To use the function, import it into your Python script:

from pascal_triangle import pascal_triangle



Output:

[
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1]
]
Example

Here’s an example demonstrating how to print the triangle in a formatted way:

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

Output:

[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
