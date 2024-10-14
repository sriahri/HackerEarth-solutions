'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
l = list(map(int, input().split()))
c = 0
for i in range(l[0], l[1] + 1):
    if i % l[2] == 0:
        c += 1
print(c)
