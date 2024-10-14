'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
from math import ceil, sqrt

n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
for j in range(2, (ceil(sqrt(max(l)))) + 2 * (min(l))):
    c = 1
    x = l[0] % j
    for i in range(1, n):
        if l[i] % j == x:
            c += 1
        else:
            break
        if c == len(l):
            print(j, end=' ')
