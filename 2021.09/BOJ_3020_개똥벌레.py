N, H = map(int, input().split())
cave = [[0] * N for _ in range(H)]
for i in range(N):
    long = int(input())
    if i % 2 == 0:
        for j in range(long):
            cave[H-j-1][i] = 1
    else:
        for j in range(long):
            cave[j][i] = 1
result = []
for i in range(H):
    cnt = 0
    for j in range(N):
        if cave[i][j] == 1:
            cnt += 1
    result.append(cnt)
min_result = min(result)
min_ans = []
for i in result:
    if i == min_result:
        min_ans.append(i)
print(min_result, len(min_ans))