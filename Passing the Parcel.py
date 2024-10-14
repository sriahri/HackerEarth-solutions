'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n = int(input())
s = input()
l = len(s)
li = [1] * n
c = 0
i = 0
j = 0
while c < n - 1:
    if i >= l:
        i = i % l
    if j >= n:
        j = j % n
    if s[i] == 'a':
        if li[j] == 1:
            i += 1
            j += 1
        else:
            j += 1
    else:
        if li[j] == 1:
            li[j] = 0
            i += 1
            j += 1
            c += 1
        else:
            j += 1
for i in range(len(li)):
    if li[i] == 1:
        print(i + 1)
        break
