n, m = map(int, input().split())
for i in range(n):
    if i % 2 == 0:
        for j in range(1, m+1):
            print(j + (i * m), end=' ')
    else:
        for j in range(m, 0, -1):
            print(j + (i * m), end=' ')
    print()