#!python
# Sum of Values

"""
The file task03.txt contains a lot of data.  Each cluster of data is the number of points for that particular group.  Each blank line indicates a separator before the next group.
Read the contents of task03.txt into your program and determine the points value of the cluster with largest sum.

For sample data task03.txt, the largest sum should be 68787
"""

import math


f = open('task03.txt','r')
data = f.read()


sub_lists = [s.split('\n') for s in data.strip().split('\n\n')]


int_lists = [[int(item) for item in sub_list] for sub_list in sub_lists]
list1 = []
for i in int_lists:
    total = 0
    for x in i:
        total = total+x
    list1.append(total)
    print(list1)
    list1.sort()
    print(list1)


print("Largest element is:", list1[-1])