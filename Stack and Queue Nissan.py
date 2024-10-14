'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n, k = map(int, input().split())
l = list(map(int, input().split()))
i = 0
c = sum(l[:k])
m = c
for i in range(k - 1):
    c = c - l[k - 1 - i] + l[n - 1 - i]
    if c > m:
        m = c
print(m)
