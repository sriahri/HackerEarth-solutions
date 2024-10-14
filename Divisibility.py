'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

N = int(input())
data = [int(x) for x in input().split()]

s = ''
# Write your code here
# ans =
for i in data:
    s += str(i % 10)
if s[-1] == '0':
    ans = 'Yes'
else:
    ans = 'No'
print(ans)