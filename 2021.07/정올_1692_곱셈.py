num1 = int(input())
num2 = int(input())
hund = num2 // 100  # 3
ten = (num2 - (hund * 100)) // 10
one = num2 - (hund * 100) - (ten * 10)
ans_1 = num1 * one
ans_10 = (num1 * ten)
ans_100 = (num1 * hund)
print(ans_1)
print(ans_10)
print(ans_100)
print(ans_1 + (ans_10 * 10) + (ans_100 * 100))