# 우하좌상(시계방향)으로 사방탐색
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def BFS(x, y):
    global ans
    Q = []
    Q.append((x, y))
    visit[x][y] = 1

    # Q가 비어있기 전까지 무한 반복
    while Q:
        r, c = Q.pop(0)
        # 사방탐색하기
        for i in range(4):
            next_r = r + dr[i]
            next_c = c + dc[i]
            # 범위를 벗어난 경우 방향 바꾸기(범위 먼저!!!)
            if next_r < 0 or next_r >= 100 or next_c < 0 or next_c >= 100:
                continue
            # 벽을 만나거나 이미 방문한 경우에도 방향 바꾸기(or!!!!!)
            if miro[next_r][next_c] == 1 or visit[next_r][next_c] != 0:
                continue
            # 3을 만나면 도착! ans = 1, 끝내기!
            if miro[next_r][next_c] == 3:
                ans = 1
                return
            # 다음에 나올 위치 다시 Q에 집어 넣기
            Q.append((next_r, next_c))
            # 방문 체크(미로의 길이까지도 파악 가능)
            visit[next_r][next_c] = visit[r][c] + 1


# 시작점 찾기(시작점은 2)
# 시작점부터 bfs 돌기
# 지나간 길 다시 가지 않도록 1로 바꾸기 -> visit에서 1이 아니라 +1로!!!
# 범위 밖이거나 벽에 부딪히면 방향 틀기(4방탐색으로)
# 3을 만나면 1 반환
# 전체 다 돌았는데도 3이 없으면 0 반환

for T in range(1, 11):
    tc = int(input())
    # 미로 인풋
    miro = [list(map(int, input())) for _ in range(100)]
    # 방문체크 & 미로 길이 파악용 0으로 된 2차원 리스트
    visit = [[0] * 100 for _ in range(100)]
    ans = 0
    x = 0
    y = 0
    # 시작점찾기
    for i in range(100):
        for j in range(100):
            if miro[i][j] == 2:
                x = i
                y = j
    BFS(x, y)
    print("#{} {}".format(T, ans))