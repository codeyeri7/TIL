import string

n = int(input())
alpha = string.ascii_uppercase
a = 1
for i in range(n):
    for j in range(n*n-a, -1, -n):
        print(alpha[j % 26], end=' ')
    a += 1
    print()
