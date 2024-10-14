'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
s = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for _ in range(int(input())):
    l = input().split()
    n = len(l)
    c = 0
    for i in range(n):
        for j in range(len(l[i])):
            c += j + s.find(l[i][j])
    print(c * n)
