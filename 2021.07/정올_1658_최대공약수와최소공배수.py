a, b = map(int, input().split())
gcb = []  # 공약수 구하기
for i in range(1, a + 1):
# a와 b를 i로 나누었을 때 나온 나머지가 0일 때(동시에) 그게 공약수
    if a % i == 0 and b % i == 0:
        gcb.append(i)
# a와 b를 곱한 수를 최대공약수로 나누면 그게 최소공배수이다.
lcm = int(a * b / max(gcb))
print(max(gcb))
print(lcm)

####################

# a, b가 1억 이상이라면 다른 방법으로 풀어야 함 (정올 참조)
a, b = map(int, input().split())
x = a
y = b
while y != 0:  # y가 0이면 x가 최대공약수이므로 종료
    r = x % y  # 나머지를 구한 후
    x = y  # x를 y로
    y = r  # y를 r로 바꾸고 다시 반복
gcb = x
lcm = int(a * b / gcb)
print(gcb)
print(lcm)
