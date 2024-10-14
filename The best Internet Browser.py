'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
for _ in range(int(input())):
    l = input()
    s = l.split('.')
    x = s[1]
    # print(x)
    c = 0
    for i in x:
        if i not in ['a', 'e', 'i', 'o', 'u']:
            c += 1
    a = c + 4
    b = len(l)
    print('{}/{}'.format(a, b))
