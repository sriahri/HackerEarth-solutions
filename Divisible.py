def solve(A):
    # Write your code here
    s = ''
    for i in range(len(A)):
        if i < len(A) // 2:
            a = str(A[i])
            s += a[0]
        else:
            a += str(A[i])
            s += a[-1]
    if int(s) % 11 == 0:
        return 'OUI'
    else:
        return 'NON'


N = int(input())
A = list(map(int, input().split()))
out_ = solve(A)
print(out_)