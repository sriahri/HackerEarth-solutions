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
    l = s[0]
    for i in s[1:]:
        if l:
            if i != l[-1]:
                l += i
    print(l)
