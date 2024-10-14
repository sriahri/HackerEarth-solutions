'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t = int(input())
l = [bin(i)[2:] for i in range(299999)]
for _ in range(t):
    a = []
    x = []
    n, k = map(int, input().split())
    for i in l:
        if '11' not in i:
            a.append(i)
    for i in a:
        s = ''
        s += '0' * (n - len(i)) + i
        s = s.replace('0', 'O')
        s = s.replace('1', 'Z')
        x.append(s)
    if k > 2 ** n:
        print(-1)
    else:
        print(x[k - 1])
