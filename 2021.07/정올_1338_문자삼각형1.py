import string
n = int(input())
alpha = string.ascii_uppercase
a = 0
b = 1
for i in range(n-1, -1, -1):
    num = (a % 26)
    c = n - 1
    for j in range(i):
        print(" ", end=" ")
    for k in range(b):
        if k > 0:
            print(alpha[(num + c) % 26], end=" ")
            num += c
            c -= 1
        else:
            print(alpha[num], end=" ")

    print()
    a += 1
    b += 1


