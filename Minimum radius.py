'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
from math import sqrt, ceil

for _ in range(int(input())):
    n, p = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    a = list(map(int, input().split()))
    radii = []
    for i in range(n):
        radii.append(sqrt(x[i] * x[i] + y[i] * y[i]))
    d = []
    for i in range(n):
        d.append([radii[i], a[i]])
    res = sorted(d, key=lambda x: x[0])
    ans = 0
    for i in res:
        r = ceil(i[0])
        ans += i[1]
        if ans >= p:
            print(r)
            break
    else:
        print(-1)