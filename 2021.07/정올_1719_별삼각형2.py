n, m = map(int, input().split())
a = 0
mid = n // 2
for i in range(mid + 1):
    a += 1
    for j in range(1, a+1):
        print('*', end='')
    print()

b = mid
for i in range(n - (mid + 1) + 1, n):
    for j in range(b, 0, -1):
        print('*', end='')
        b -= 1
    print()