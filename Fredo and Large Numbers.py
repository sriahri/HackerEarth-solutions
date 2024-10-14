'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
from collections import Counter

n = int(input())
l = list(map(int, input().split()))
d = Counter(l)
c = []
for i in l:
    c.append(d[i])
q = int(input())
for i in range(q):
    a, b = map(int, input().split())
    flag = 0
    if a == 1:
        if b in c:
            x = c.index(b)
            print(l[x])
        else:
            print(0)
    else:
        for i in range(n):
            if c[i] >= b:
                print(l[i])
                flag = 1
                break
        if flag == 0:
            print(0)
