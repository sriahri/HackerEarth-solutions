'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
for _ in range(int(input())):
    n, x, y = map(int, input().split())
    l = list(map(int, input().split()))
    maxi = 0
    ans = 0
    a = []
    i = 0
    while i < n:
        if l[i] > x:
            if y:
                y -= 1
                ans += 1
                a.append([y])
            else:
                maxi = max(ans, maxi)
                ans -= 1
                i -= 1
                p = a.pop(0)
                if len(p) == 2:
                    x += p[1]
                else:
                    y += 1
        else:
            if l[i] == 0:
                ans += 1
            elif x:
                x -= l[i]
                ans += 1
                a.append([x, l[i]])
            else:
                maxi = max(ans, maxi)
                ans -= 1
                p = a.pop(0)
                i -= 1
                if len(p) == 2:
                    x += p[1]
                else:
                    y += 1
        i += 1
    print(max(maxi, ans))