'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    c = 1
    x = s[0]
    if len(s) == 1:
        pass
    else:
        for i in range(1, n):
            if x > s[i]:
                c += 1
                x = s[i]
    print(c)
