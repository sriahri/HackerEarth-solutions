'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n = int(input())
s = input()
st = ''
if 'HH' in s:
    print('NO')
else:
    for i in s:
        if i == '.':
            st += 'B'
        else:
            st += i
    print('YES')
    print(st)
