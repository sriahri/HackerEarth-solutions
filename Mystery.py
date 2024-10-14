'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
from math import sqrt


def factors(n):
    c = 0
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            if n // i == i:
                c += 1
            else:
                c += 2
    return c


t = int(input())
for i in range(t):
    n = int(input())
    print(factors(n))
