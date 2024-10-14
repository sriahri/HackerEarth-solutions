'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
from math import gcd

n = int(input())
l = list(map(int, input().split()))
if n == 0:
    g = 1
elif n == 1:
    g = l[0]
else:
    for i in range(len(l) - 1):
        g = gcd(l[i], l[i + 1])
f = 1
for j in l:
    f *= j
print((f ** g) % (1000000007))
