'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    if l.count(min(l)) % 2 == 1:
        print('Lucky')
    else:
        print('Unlucky')