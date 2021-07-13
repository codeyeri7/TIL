import string
n = int(input())
alpha = string.ascii_uppercase
a = 0
b = 1
c = n + 1
for i in range(n-1, -1, -1):
    for j in range(i):
        print(" ", end=" ")
    for k in range(b):
        print(alpha[(a % 26)])
        a = (a % 26) + c
        c -= 1
    a += 1
    b += 1
