'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
from collections import Counter

for _ in range(int(input())):
    n = int(input())
    c = 0
    a = list(map(int, input().split()))
    d = Counter(a)
    for i in d.keys():
        if d[i] > i:
            c += d[i] - i
        elif i - d[i] > i // 2:
            c += d[i]
        else:
            c += i - d[i]
    print(c)
