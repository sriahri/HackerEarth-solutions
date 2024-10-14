'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
from math import gcd


def gcdd(p, q):
    return gcd(p, q)


n, q = map(int, input().split())
l = list(map(int, input().split()))
g = l[0]
for i in range(1, n):
    g = gcd(g, l[i])
for i in range(q):
    p = int(input())
    if p % g == 0:
        print('YES')
    else:
        print('NO')