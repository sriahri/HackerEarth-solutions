'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
for _ in range(int(input())):
    l = []
    n = int(input())
    for i in range(n):
        l.append(list(map(int, input().split())))
    x = sorted(l, key=lambda i: i[1])
    c = 0
    b = 0
    # print(x)
    for i in x:
        if i[1] > b:
            c += 1
            b += i[1]
    print(c)