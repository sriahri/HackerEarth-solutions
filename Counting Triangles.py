'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n = int(input())
d = {}
c = 0
for i in range(n):
    l = list(map(str, input().split()))
    l.sort()
    x = ''.join(l)
    if x in d.keys():
        d[x] += 1
    else:
        d[x] = 1
for i in d.keys():
    if d[i] == 1:
        c += 1
print(c)
