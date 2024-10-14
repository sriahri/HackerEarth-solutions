x = int(input())
for i in range(x):
    n = int(input()) - 1
    a = (n - (n % 3)) // 3
    b = (n - (n % 5)) // 5
    c = (n - n % 15) // 15
    p = 3 * (a * (a + 1)) // 2
    q = 5 * (b * (b + 1)) // 2
    r = 15 * (c * (c + 1)) // 2
    print(p + q - r)
