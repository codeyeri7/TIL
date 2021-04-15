# 런타임ㅠ

import copy
def find_minsum(x, y, minmin):  # 배열 탐색하며 숫자합 저장
    global visited
    if visit[x][y] >= minmin:
        return
    dr = [0, 1]
    dc = [1, 0]
    # 목적지 도착하면 숫자합 저장
    if x == N-1 and y == N-1:
        visited.append(visit[x][y])
        minmin = min(visited) # 경로의 최소합을 변수로 지정
    if x+dr[0] >= 0 and x+dr[0] < N and y+dc[0] >= 0 and y+dc[0] < N:
        # 오른쪽으로 이동
        r, c = x+dr[0], y+dc[0]
        # 오른쪽으로 이동한 visit에 지금까지 온 길의 합을 더하기
        visit[r][c] = visit[x][y] + arr[r][c]
        # 만약 지금까지 온 길의 합이 경로의 최소합보다 크다면 더이상 가지 말아랏
        if visit[r][c] > minmin:
            return
        # print(minmin)
        find_minsum(r, c, minmin)  # 재귀
    if x+dr[1] >= 0 and x+dr[1] < N and y+dc[1] >= 0 and y+dc[1] < N:
        # 아래쪽으로 이동
        a, b = x+dr[1], y+dc[1]
        visit[a][b] = visit[x][y] + arr[a][b]
        # 만약 지금까지 온 길의 합이 경로의 최소합보다 크다면 더이상 가지 말아랏
        if visit[a][b] > minmin:
            return
        # print(minmin)
        find_minsum(a, b, minmin)


for T in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 중복체크용
    visit = copy.deepcopy(arr)
    visited = []
    ans = 100000  # 경로의 합 저장하기 위한 변수
    # 최소합 구하기 시작!
    find_minsum(0, 0, ans)
    print("#{} {}".format(T, min(visited)))
