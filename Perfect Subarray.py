'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
import math

c = 0
n = int(input())
l = list(map(int, input().split()))
for i in range(n):
    s = 0
    for j in range(i, n):
        s += l[j]
        x = int(math.sqrt(s))
        if x * x == s:
            c += 1
print(c)