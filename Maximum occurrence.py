'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
from collections import Counter

s = input()
d = Counter(s)
maxi = 0
ans = 0
for i in sorted(d.keys()):
    if d[i] > maxi:
        maxi = d[i]
        ans = i
print(ans, maxi)
