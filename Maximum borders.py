for _ in range(int(input())):
    n, m = map(int, input().split())
    l = []
    for i in range(n):
        l.append(input())

    max_count = 0
    for i in range(n):
        count = 1
        for j in range(m - 1):
            if l[i][j] and l[i][j + 1] == '#':
                count += 1
            else:
                if count > max_count:
                    max_count = count
                    count = 1
    for i in range(n - 1):
        count = 1
        for j in range(m):
            if l[i][j] and l[i + 1][j] == '#':
                count += 1
            else:
                if count > max_count:
                    max_count = count
                    count = 1

    print(max_count - 1)