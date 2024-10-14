'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
import math

t = int(input())
for i in range(t):
    l, b, h = map(int, input().split())
    a = math.gcd(l, b)
    a = math.gcd(a, h)
    print(a, end=' ')
    print(((l * b * h) // (a * a * a)) % 1000000007)
