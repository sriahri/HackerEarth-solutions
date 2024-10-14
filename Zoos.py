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
if 2 * d['z'] == d['o']:
    print('Yes')
else:
    print('No')
