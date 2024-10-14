'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n, k = map(int, input().split())
l = list(map(int, input().split()))
skip = 0
c = 0
for i in l:
    if i <= k and skip < 2:
        c += 1
    else:
        skip += 1
print(c)