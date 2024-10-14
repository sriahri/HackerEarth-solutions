'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n = int(input())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
for i in range(n):
    print(l1[i] + l2[i], end=' ')