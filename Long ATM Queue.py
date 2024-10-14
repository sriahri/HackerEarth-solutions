'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n = int(input())
l = list(map(int, input().split()))
c = 1
for i in range(n - 1):
    if l[i] > l[i + 1]:
        c += 1
print(c)