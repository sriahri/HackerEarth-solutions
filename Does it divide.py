'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
from math import factorial

t = int(input())
for _ in range(t):
    n = int(input())
    p = factorial(n)
    s = (n * (n + 1)) // 2
    if p % s == 0:
        print('YES')
    else:
        print('NO')
