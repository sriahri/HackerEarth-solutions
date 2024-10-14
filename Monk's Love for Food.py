'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t = int(input())
s = []
c = 0
for _ in range(t):
    package = list(map(int, input().split()))
    if len(package) == 2:
        s.append(package[1])
    else:
        while 1:
            break
        if len(package) == 2:
            c += 1
        if len(s) != 0:
            result = s[len(s) - 1]
            if len(s) == len(package) - 1:
                c -= 1
            s.pop()
            if len(package) == len(s):
                c += 1
            print(result)
        else:
            print('No Food')
