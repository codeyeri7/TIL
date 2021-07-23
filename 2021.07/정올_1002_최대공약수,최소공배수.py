n = int(input())
numbers = list(map(int, input().split()))
gcd = lcm = numbers[0]
for i in range(1, n):
    divisor = []
    for j in range(1, gcd+1):
        if gcd % j == 0 and numbers[i] % j == 0:
            divisor.append(j)
    lcm = int(gcd * numbers[i] / max(divisor))
    gcd = max(divisor)

print(gcd, lcm)

# 3
# 78 39 104