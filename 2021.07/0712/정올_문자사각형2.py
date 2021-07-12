import string

n = int(input())
alpha = string.ascii_uppercase
a = 0
for i in range(n):
    b = 0
    c = 0
    for j in range(n):
        if j % 2 == 0:
            k = ((n * 2) * b) + a
            b += 1
            print(alpha[k % 26], end=' ')

        else:
            k = ((n * 2) * (c + 1)) - (a + 1)
            c += 1
            print(alpha[k % 26], end=' ')

    a += 1
    print()