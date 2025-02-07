"""
Read the data from one of the task02 text files.
The data from this file contains 3 numbers on each line.  Determine how many lines of this file contains Pythagorean triples.
Pythagorean triples are numbers where all of the sides are integers, and the 3 sides form a right triangle.
The triples contained are : { 2a : 6, 2b: 4, 2c: 11}
"""

count = 0
with open('task02a.txt', 'r') as file:
    for line in file:
        numbers = list(map(int, line.split()))
        if len(numbers) == 3:
            a, b, c = sorted(numbers)
            if a ** 2 + b ** 2 == c ** 2:
                count += 1
                print(count)