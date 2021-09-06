N = int(input())
numN = list(map(int, input().split()))
M = int(input())
numM = list(map(int, input().split()))
numN.sort()  # 오름차순 정렬

for i in numM:
    start = 0
    end = N - 1
    for j in range(N):
        if start > end:  # start가 더 커진다면 그 안에 찾는 수가 없다는 뜻
            print(0)
            break
        middle = (start + end) // 2
        if i == numN[middle]:  # 해당 수가 있으면 1 출력
            print(1)
            break
        elif i < numN[middle]:  # i가 왼쪽에 있을 때
            end = middle - 1
        elif i > numN[middle]:  # i가 오른쪽에 있을 때
            start = middle + 1
