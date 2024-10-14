# '''
# # Sample code to perform I/O:

# name = input()                  # Reading input from STDIN
# print('Hi, %s.' % name)         # Writing output to STDOUT

# # Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
# '''

# # Write your code here
# n=int(input())
# l=list(map(int,input().split()))
# x=[]
# ans=0
# for i in range(n):
#     if l[i]>0:
#         x.append(l[i])
#     elif l[i]<0:
#         if x and -l[x[-1]]==l[i]:
#             x.pop()
#             if not x:
#                 temp=-1
#             else:
#                 temp=x[-1]
#             ans=max(ans,i-temp)
# print(ans)


n = int(input())
a = list(map(int, input().split()))
s = []
ans = 0

for i in range(0, n):
    if a[i] > 0:
        s.append(i)
    elif a[i] < 0:
        if s and a[i] == -a[s[-1]]:
            s.pop()
            if not s:
                temp = -1
            else:
                temp = s[-1]
            ans = max(ans, i - temp)
        else:
            s.append(i)

print(ans)