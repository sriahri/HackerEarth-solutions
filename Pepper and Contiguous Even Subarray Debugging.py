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
    x = [-1]
    for i in range(n):
        if l[i] % 2 == 0:
            c += 1
            x.append(c)
        else:
            c = 0
    print(max(x))
