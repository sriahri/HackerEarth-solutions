'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
from collections import Counter

t = int(input())
for _ in range(t):
    k, ju = map(int, input().split())
    l = list(map(int, input().split()))
    g = list(map(int, input().split()))
    y = sorted(l)
    # g.sort()
    c = 0
    # d1=Counter(l)
    # d2=Counter(g)
    x = [0] * len(l)
    i = 0
    j = i
    while i < k - 1 and j < (ju - 1):
        c = 0
        while l[i] >= g[j] and j < ju - 1:
            c += 1
            j += 1
        x[i] = x[i - 1] + c
        i += 1
    # print(x)
    print(x.index(max(x)))
    a = x.index(max(x))
    ans = y[a]
    res = l.index(ans)
    # print(res)