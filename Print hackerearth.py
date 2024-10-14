'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n = int(input())
s = input()
h = s.count('h')
a = s.count('a')
c = s.count('c')
k = s.count('k')
e = s.count('e')
r = s.count('r')
t = s.count('t')
l = []
l.append(h // 2)
l.append(a // 2)
l.append(c)
l.append(k)
l.append(e // 2)
l.append(r // 2)
l.append(t)
print(min(l))
