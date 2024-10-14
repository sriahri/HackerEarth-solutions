'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n = int(input())
l = [20, 30, 40, 90, 80, 270, 160]
if n > len(l):
    for i in range(7, n):
        if i % 2 == 0:
            l.append(2 * l[i - 2])
        else:
            l.append(3 * l[i - 2])
maxi = 0
for i in range(n):
    for j in range(i + 1, n):
        if l[i] + l[j] + abs(l[i] - l[j]) > maxi:
            maxi = l[i] + l[j] + abs(l[i] - l[j])
print(maxi)
