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
    x = ''
    s, n = input().split()
    k = int(n)
    if math.ceil(len(s) / k) >= k:
        for i in range(len(s)):
            if i % k == 0 and i != 0:
                x += '-'
            x += s[i]
        l = list(x.split('-'))
        if (len(l[-1]) == k) or (len(l[-1]) == k - 1):
            print(x)
        else:
            print(-1)
    else:
        print(-1)
    print()