from collections import Counter

n = int(input())
l = list(map(int, input().split()))

d = Counter(l)
max_count = max(d.values())
result = 0
for i in d.keys():
    if d[i] == max_count:
        result += 1

print(result)