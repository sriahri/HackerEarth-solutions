'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n = int(input())
l = input().split()
maxi = 0
for i in range(10):
    i = str(i)
    c = 0
    for j in l:
        if i in j:
            c += 1
    if c > maxi:
        maxi = c
print(maxi)
