'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
s = input()
c = 0
c1 = 0
for i in range(len(s) - 1):
    if s[i] == '0':
        c += 1
        if c == 6:
            print('Sorry, sorry!')
            break
        if s[i + 1] == '1':
            c = 0
    else:
        c1 += 1
        if c1 == 6:
            print('Sorry, sorry!')
            break
        if s[i + 1] == '0':
            c1 = 0
else:
    print('Good luck!')