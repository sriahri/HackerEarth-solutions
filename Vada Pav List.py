'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
from collections import Counter

n = int(input())
l = [input() for i in range(n)]
d = Counter(l)
print(len(d.keys()))
for i in sorted(d.keys()):
    print(i)
