A = int(input())
B = int(input())
one = B % 10
ten = ((B - one) // 10) % 10
hund = B // 100
print(A * one)
print(A * ten)
print(A * hund)
print(A * B)