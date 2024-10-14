'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n = int(input())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
x = []
for i in range(n):
    x.append([l1[i], l2[i]])
x = sorted(x, key=lambda x: x[0])
temp = x[0][0]
temp1 = x[0][1]
i = 0
ans = 0
flag = 0
c = 0
# print(temp,temp1)
while temp > temp1 and flag == 0:
    for i in range(n):
        if x[i][1] != 0 and (x[i][0] - temp) % x[i][1] == 0:
            ans += (x[i][0] - temp) // x[i][1]
            x[i][0] = (x[i][0] - temp) // (2 * x[i][1])
            c += 1
    if c == n:
        print(ans)
        flag = 1
        break
    else:
        temp = temp - temp1
        ans = 1
if flag == 0:
    print(-1)