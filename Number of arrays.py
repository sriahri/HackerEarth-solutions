'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t = int(input())
for i in range(t):
    x = list(map(int, input().split()))
    l = list(map(int, input().split()))
    m = x[2]
    n = min(l)
    if n <= m:
        print(n)
    else:
        print('NO')
