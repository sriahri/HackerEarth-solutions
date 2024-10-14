'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
from collections import deque

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    d = deque(l)
    d.rotate(k)
    print(*d)
