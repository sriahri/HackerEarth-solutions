def function2(ans, b, length, k, p):
    for i in range(length):
        currb, currl = b[i], len(b[i])
        pos = k//p[i]
        ans += currb[pos]
        k %= p[i]
    return ans
def function (x, k, s, n, b):
  k -= 1
  length = len(b)
  p = [1]*length
  nxt = nxtp = 1
  i = length - 1
  while i >= 0:
    p[i] = nxt * nxtp
    nxt = len(b[i])
    nxtp = p[i]
    i -= 1
  ans = ''
  return function2(ans,b, length, k, p)
n,x,k = map(int,input().split())
s = input()
b = []
i = 1
for i in range(1, n+1):
    start, end = ((i-1) * x+1), min(n, (i*x))
    if start > n:
        break
    b.append(list(set(s[start-1:end])))
    b[-1].sort()
print(function(x, k, s, n, b))