'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n = int(input())
l = list(map(int, input().split()))
for i in range(n - 1):
    if l[i] <= l[i + 1]:
        l[i + 1] -= l[i]
    else:
        print('NO')
        break
else:
    if l[-1] == 0:
        print('YES')
    else:
        print('NO')