'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n = int(input())
x = int(input())
for i in range(x):
    l = list(map(int, input().split()))
    if l[0] < n or l[1] < n:
        print('UPLOAD ANOTHER')
    elif l[0] >= n and l[1] >= n:
        if l[0] == l[1]:
            print('ACCEPTED')
        else:
            print('CROP IT')
