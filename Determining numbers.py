'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
from collections import Counter

n = int(input())
l = list(map(int, input().split()))
d = Counter(l)
a = []
for i in d.keys():
    if d[i] == 1:
        a.append(i)
a.sort()
print(*a)
