'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    l = list(map(int, input().split()))
    flag = 1
    ne = 0
    po = 0
    ans = 0
    for i in l:
        if i < 0:
            ne += 1
        else:
            po += 1
        if ne > 1:
            break
    if ne == 1 or po == n:
        res = min(l)
        flag = 0
    elif ne == n:
        res = sum(l)
        flag = 0
    elif po == 1:
        res = sum(l) - max(l)
        flag = 0
    # ne=0
    # if flag!=0:
    #     y=sorted(l)
    #     for i in range(len(y)-1):
    #         if s>=0 and y[i]<0:
    #             a=l.index(y[i])
    #             b=l.index(y[i+1])
    #             if abs(a-b)!=1:
    #                 ans+=y[i]
    #                 s-=1
    #             else:
    #                 ans+=y[i]
    #     print(ans)
    # if flag!=1:
    #     print(res)
    l.sort()
    i = 0
    ans = 0
    while l[i] < 0:
        ans += l[i]
        i += 1
    print(ans)
