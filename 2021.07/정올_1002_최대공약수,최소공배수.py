# 최대공약수 구하기
def gcd_num(a, b):
    divisor = []
    for j in range(1, a+1):
        if a % j == 0 and b % j == 0:
            divisor.append(j)
    return max(divisor)


n = int(input())
numbers = list(map(int, input().split()))
gcd = lcm = numbers[0]  # 최대공약수, 최소공배수를 일단 첫번째 숫자로 지정
# 첫번째와 두번째의 최대공약수를 구한후,
# 그 최대공약수와 세번째 숫자의 최대공약수를 구하면
# 세 자연수의 최대공약수를 구하는 것! 이걸 반복하자
for i in range(1, n):
    gcd = gcd_num(gcd, numbers[i])

# 최소공배수도 마찬가지
# 여기서 주의할 점(내가 계속 틀림....)
# (중요)여기서의 최대공약수는 따로 구해줘야 한다.(중요)
# 최대공약수 구하고 그 최대공약수로 최소공배수 구해줬더니 계속 틀렸다ㅠㅠ
for i in range(1, n):
    gcd_1 = gcd_num(lcm, numbers[i])
    lcm = int(lcm * numbers[i] / gcd_1)

print(gcd, lcm)