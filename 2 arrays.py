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
a = 0
b = 0
asum = 0
bsum = 0
for i in range(n):
    if l1[i] < 0:
        a += 1
    else:
        asum += l1[i]
    if l2[i] < 0:
        b += 1
    else:
        bsum += l2[i]
d = abs(asum - bsum)
if a == b:
    print('Infinite')
elif bsum - asum > 0 and a != b:
    if a == 0:
        print(0)
    elif a == 1:
        print(1)
    else:
        print(d + 1)
elif asum - bsum > 0 and a != b:
    if b == 0:
        print(0)
    elif b == 1:
        print(1)
    else:
        print(d + 1)
