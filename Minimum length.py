res = []
from math import sqrt
from bisect import bisect_left


def BinarySearch(a, x):
    i = bisect_left(a, x)
    if i:
        return i
    else:
        return -1


for i in range(1, 63245):
    y = i // 2
    x = y + 1
    if i % 2 == 0:
        res.append((x * (x + 1)) - x - 1)
    else:
        res.append(x * (x + 1) - 1)
# print(res)
for _ in range(int(input())):
    n = int(input())
    ans = BinarySearch(res, n)
    print(ans + 1)