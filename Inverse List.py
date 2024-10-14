'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t = int(input())
for i in range(t):
    n = int(input())
    x = [0] * n
    l = list(map(int, input().split()))
    for j in range(n):
        if l[j] <= n:
            x[l[j] - 1] = j + 1
        else:
            print('not inverse')
    if x == l:
        print('inverse')
    else:
        print('not inverse')
