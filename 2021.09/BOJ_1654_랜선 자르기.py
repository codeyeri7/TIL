K, N = map(int, input().split())
lan = []  # 현재 갖고 있는 랜선들 모음
for i in range(K):
    l = int(input())
    lan.append(l)
# 우선 1부터 현재 가장 긴 랜선까지가 범위
start, end = 1, max(lan)
result = 0
# start가 end보다 크면 반복문 종료
while start <= end:
    mid = (start + end) // 2
    lan_cnt = []
    # 자른 랜선의 개수를 담기
    for i in lan:
        lan_cnt.append(i // mid)
    # 랜선의 개수가 나와야 할 결과보다 크거나 같으면
    if N <= sum(lan_cnt):
        # 시작 범위 +1
        start = mid + 1
        # 결과는 mid 값
        result = mid
    else:  # 랜선 개수기 결과에 미치지 못하면
        # 끝 범위 -1
        end = mid - 1
print(result)



