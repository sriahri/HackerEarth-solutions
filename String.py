'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
from collections import Counter

n = int(input())
mini = n
s = input()
d = Counter(s)
x = d.most_common(1)[0][1]
print(len(s) - x)
