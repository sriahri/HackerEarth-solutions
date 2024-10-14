'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
from collections import Counter

t = int(input())
l = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
for _ in range(t):
    s = input()
    d = Counter(s)
    c = 0
    for i in d.keys():
        if i in l:
            c += d[i]
    print(c)
