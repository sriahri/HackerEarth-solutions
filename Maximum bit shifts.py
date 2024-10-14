'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t = int(input())
l = list(map(int, input().split()))
for i in l:
    a = bin(i).replace("0b", "")
    x = list(a)
    x.sort(reverse=True)
    s = ''.join(x)
    print(int(s, 2), end=' ')

