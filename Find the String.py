'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    l = []
    for i in range(n):
        l.append(input())
    # print(l)
    flag = 0
    s = input()
    for i in range(len(s)):
        if s[i] not in l[i % n]:
            flag = 1
            break
        else:
            x = l[i % n]
            x = x.replace(s[i], '', 1)
            l[i % n] = x
    if flag:
        print('No')
    else:
        print('Yes')