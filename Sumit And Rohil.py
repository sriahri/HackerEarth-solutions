'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
# from collections import Counter
# n=int(input())
# l=[input() for i in range(n)]
# x=[]
# a=[]
# c=0
# for i in range(n):
#     p=''
#     p+=l[i][0]
#     p+=l[i][-1]
#     a.append([p,l[i]])
# a=sorted(a,key=lambda x:x[0])
# #print(a)
# for i in range(n-1):
#     if len(a[i][1])==len(a[i+1][1]) and a[i][0]==a[i+1][0]:
#         x.append(a[i+1][0])
#         if a[i][1] not in x:
#             x.append(a[i][0])
# d=Counter(x)
# for i in d.keys():
#     c+=1
# print(c)
# print(x)
# if x:
#     for i in range(len(x)):
#         x[i]=sorted(x[i])
#         x[i]=str(x[i])
#     d=Counter(x)
#     for i in d.keys():
#         c+=1
# print(c)

n = int(input())
c = 0
l = set()
for i in range(n):
    s = input()
    p = ''
    p += s[0] + s[-1]
    p += str(sorted(s))
    if p not in l:
        l.add(p)
        c += 1
print(c)
