'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
from math import floor

t = int(input())
for _ in range(t):
    c = 0
    a, b, m = map(int, input().split())
    c = b // m - a // m
    if a % m == 0:
        c += 1
    print(c)
