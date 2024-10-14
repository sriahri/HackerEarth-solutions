'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t = int(input())
for i in range(t):
    n = int(input())
    s = ''
    x = n
    if n % 6 == 0 or n % 6 == 1:
        s = 'WS'
    elif n % 6 == 2 or n % 6 == 5:
        s = 'MS'
    else:
        s = 'AS'
    if (n // 6) % 2 == 0:
        if n % 6 == 1:
            x += 11
        elif n % 6 == 2:
            x += 9
        elif n % 6 == 3:
            x += 7
        elif n % 6 == 4:
            x += 5
        elif n % 6 == 5:
            x += 3
        else:
            x -= 11
    else:
        if n % 6 == 1:
            x -= 1
        elif n % 6 == 2:
            x -= 3
        elif n % 6 == 3:
            x -= 5
        elif n % 6 == 4:
            x -= 7
        elif n % 6 == 5:
            x -= 9
        else:
            x += 1
    print(x, s)