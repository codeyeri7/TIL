n, m = map(int, input().split())
for i in range(n):
    for j in range(1, m+1):
        print(j + (i * m), end=' ')
    print()