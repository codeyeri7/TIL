N = int(input())
ans = []
# 문제에서 N의 범위가 21억까지 가기 때문에 기존 방법대로 하면 시간초과가 뜸
# 그래서 제곱근을 이용해서 구해야 한다.
for i in range(1, int(N**0.5)+1):
    if N % i == 0:
        ans.append(i)
        # 100의 약수를 찾을 때 10 * 10인 경우에 10이 두 번 append되면 안되니까
        if i != N//i:
            ans.append(N//i)
sort = ans.sort()
print(" ".join(map(str, ans)))