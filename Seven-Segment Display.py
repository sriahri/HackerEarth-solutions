'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t = int(input())
for i in range(t):
    x = 0
    n = input()

    for a in n:
        if a == '0' or a == '6' or a == '9':
            x += 6
        elif a == '1':
            x += 2
        elif a == '2' or a == '3' or a == '5':
            x += 5

        elif a == '4':
            x += 4

        elif a == '7':
            x += 3
        elif a == '8':
            x += 7

        # print(x)
    if x % 2 == 0:
        print('1' * (x // 2))
    else:
        x -= 3
        print('7', end='')
        print('1' * (x // 2))