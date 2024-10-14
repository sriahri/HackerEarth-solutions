'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
s = input()
c = 0
a = 0
# x=['1','2','3','4','5','6']
for i in range(len(s)):
    if s[i] != '6':
        c += 1
print(c)