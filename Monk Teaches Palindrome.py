'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t = int(input())
for _ in range(t):
    s = input()
    if s == s[::-1]:
        print('YES', end=' ')
        if len(s) % 2 == 0:
            print('EVEN')
        else:
            print('ODD')
    else:
        print('NO')