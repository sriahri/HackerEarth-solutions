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
    r = list(map(int, input().split()))
    a = list(map(int, input().split()))
    d1 = Counter(r)
    maxi = 0
    for i in sorted(d1.keys(), reverse=True):
        if d1[i] > maxi:
            maxi = d1[i]
            ans1 = i
    maxi = 0
    d2 = Counter(a)
    for i in sorted(d2.keys(), reverse=True):
        if d2[i] > maxi:
            maxi = d2[i]
            ans2 = i
    if ans1 > ans2:
        print('Rupam')
    elif ans1 < ans2:
        print('Ankit')
    else:
        print('Tie')
