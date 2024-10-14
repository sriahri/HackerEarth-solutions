'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
for _ in range(int(input())):
    n, f1, f2, f3 = map(int, input().split())
    c = 0
    for i in range(1, n + 1):
        if i % f1 == 0 and i % f2 != 0 and i % f3 != 0:
            c += 1
        elif i % f1 != 0 and i % f2 == 0 and i % f3 != 0:
            c += 1
        elif i % f1 != 0 and i % f2 != 0 and i % f3 == 0:
            c += 1
    print(c)