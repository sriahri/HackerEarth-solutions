'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t = int(input())
for i in range(t):
    a = 0
    b = 0
    x = list(map(int, input().split()))
    n = int(input())
    for i in range(n):
        l = list(map(int, input().split()))
        if l[0] == 1:
            a += 1
        if l[1] == 1:
            b += 1
    if a > b:
        print((b * max(x)) + (a * min(x)))
    else:
        print((a * max(x)) + (b * min(x)))
