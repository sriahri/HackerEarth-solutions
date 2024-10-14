'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
import math

l, b = map(int, input().split())
area = l * b
i = 2
if math.gcd(l, b) > 1:
    print('Yes')
else:
    print('No')