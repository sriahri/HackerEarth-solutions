'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n = int(input())
l = list(map(int, input().split()))
s = 0
c = 0
for i in l:
    if i >= 0:
        s += i
        c += 1
if s == 0 and c == 0:
    s = max(l)
    c = 1
print(s, c)
