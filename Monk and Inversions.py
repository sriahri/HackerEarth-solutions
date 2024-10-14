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
    l = []
    c = 0
    for i in range(n):
        l.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(n):
            for p in range(n):
                for q in range(n):
                    if i <= p and j <= q:
                        if l[i][j] > l[p][q]:
                            c += 1
    print(c)