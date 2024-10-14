'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n = int(input())
l = []
for i in range(n):
    inp = int(input())
    if inp == 0:
        if l:
            l.pop()
    else:
        l.append(inp)
print(sum(l))
