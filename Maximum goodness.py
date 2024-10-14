'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n = int(input())
l = list(map(int, input().split()))
x = [0] * n
a = l.count(1)
b = l.count(0)
x[-1] = abs(a - b)
for i in range(n - 2, -1, -1):
    if l[i] == 1:
        a -= 1
    else:
        b -= 1
    x[i] = abs(a - b)
maxi = x[-1]
ans = n
# print(x)
for i in range(n - 1, -1, -1):
    if maxi < x[i]:
        ans = i
        maxi = x[i]
print(ans)