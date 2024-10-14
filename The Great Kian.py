'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n = int(input())
l = list(map(int, input().split()))
a1, a2, a3 = 0, 0, 0
for i in range(len(l)):
    if i % 3 == 0:
        a1 += l[i]
    elif i % 3 == 1:
        a2 += l[i]
    else:
        a3 += l[i]
print(a1, a2, a3)
