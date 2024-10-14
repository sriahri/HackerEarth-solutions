'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n = int(input())
l = list(map(int, input().split()))
x = []
a = []
for i in range(n):
    if l[i] % 2 == 0:
        x.append(l[i])
    else:
        if x:
            for j in x[::-1]:
                a.append(j)
        a.append(l[i])
        x = []
if x:
    for j in x[::-1]:
        a.append(j)
print(*a)