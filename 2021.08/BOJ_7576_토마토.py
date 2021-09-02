from collections import deque
M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
q = deque()
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            # 익은 토마토들을 q에 넣어주기
            q.append((i, j))

def BFS():
    d_r = [-1, 0, 1, 0]
    d_c = [0, 1, 0, -1]
    while q:
        a, b = q.popleft()
        for i in range(4):
            temp_r = a + d_r[i]
            temp_c = b + d_c[i]
            if 0 <= temp_r < N and 0 <= temp_c < M:
                if tomato[temp_r][temp_c] == 0:
                    # 자신을 익게 만든 토마토에서 +1을 해서 날짜 체크
                    tomato[temp_r][temp_c] = tomato[a][b] + 1
                    q.append((temp_r, temp_c))
BFS()
# 익는데 제일 오래 걸린 토마토 찾기
max_tomato = 0
result = True
for i in range(N):
    for j in range(M):
        # 근데 아직도 안 익은 토마토가 있다?
        if tomato[i][j] == 0:
            # result를 False로 바꿈
            result = False
            break
        elif tomato[i][j] > max_tomato:
            # 오래 걸린 토마토 갱신
            max_tomato = tomato[i][j]
if result:  # 다 익었다면 결과 출력 (1에서 처음 익게 된 토마토를 2로 시작했기 때문에 답은 -1을 해줌)
    print(max_tomato - 1)
else:  # 다 안 익은 토마토 있음 -1 출력
    print(-1)
