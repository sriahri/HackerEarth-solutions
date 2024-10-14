'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
s = input()
a = 0
if (int(s[0]) + int(s[1])) % 2 == 0:
    a += 1
if s[2] not in ["A", "E", "I", "O", "U", "Y"]:
    a += 1
if (int(s[3]) + int(s[4])) % 2 == 0 and (int(s[4]) + int(s[5])) % 2 == 0:
    a += 1
if (int(s[7]) + int(s[8])) % 2 == 0:
    a += 1
# print(a)
if a == 4:
    print('valid')
else:
    print('invalid')