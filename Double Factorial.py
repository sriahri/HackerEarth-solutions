'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
from math import factorial

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(factorial(factorial(n)) % (10 ** m))