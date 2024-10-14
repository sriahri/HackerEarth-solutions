'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n = int(input())
for i in range(n):
    s = input()
    letters = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f',
               'e', 'd', 'c', 'b', 'a']
    cou = [0] * 26
    l = []
    for i in s:
        cou[letters.index(i)] += 1
    for i in range(26):
        l.append([letters[i], cou[i]])
    a = sorted(l, key=lambda x: x[1])
    for i in range(26):
        print(a[i][0], end=' ')
    print()
