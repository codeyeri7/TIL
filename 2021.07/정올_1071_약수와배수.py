n = int(input())
nums = list(map(int, input().split()))
m = int(input())
m_divisor = []  # m의 약수
m_multiple = []  # nums 중에서 m의 배수
nums_divisor = []  # nums 중에서 m의 약수
# m의 약수 구하기
for i in range(1, m+1):
    if m % i == 0:
        m_divisor.append(i)
# nums 중에서 m의 배수 구하기
for i in nums:
    if i % m == 0:
        m_multiple.append(i)
# 구한 m의 약수를 가지고 nums 중에서 m의 약수 구하기
for i in nums:
    if i in m_divisor:
        nums_divisor.append(i)
# 구한 약수와 배수끼리 더해 답 출력하기
ans_div = 0
ans_multi = 0
for i in nums_divisor:
    ans_div += i
for i in m_multiple:
    ans_multi += i
print(ans_div)
print(ans_multi)

