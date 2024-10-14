'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
s = input().split()
k = int(s[1])
a = s[0]
x = ''
if k >= len(a):
    print(('9') * (len(a)))
else:
    c = 0
    for i in range(len(a)):
        if c != k:
            if a[i] != '9':
                x += '9'
                c += 1
            else:
                x += a[i]
        else:
            x += a[i]
        # else:
        # break
    print(x)
