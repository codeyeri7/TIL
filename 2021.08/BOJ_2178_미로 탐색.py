from collections import deque

d_r = [-1, 0, 1, 0]
d_c = [0, 1, 0, -1]
def BFS(r, c):  # 너비 우선 탐색
    q = deque()
    q.append((r, c))  # q에 출발지점 넣기
    visit[r][c] = 1  # 방문체크 + 최소거리 구하기
    while q:
        a, b = q.popleft()
        if a == N-1 and b == M-1:  # 도착지
            print(visit[a][b])
            break  # 다 도착했음 함수 종료
        for i in range(4):  # 4방향 탐색
            temp_r = a + d_r[i]
            temp_c = b + d_c[i]
            # 범위안에 있고, 아직 방문하지 않았을 때
            if 0 <= temp_r < N and 0 <= temp_c < M:
                if visit[temp_r][temp_c] == 0 and miro[temp_r][temp_c] == 1:
                    visit[temp_r][temp_c] = visit[a][b] + 1  # 방문체크 + 최소거리
                    q.append((temp_r, temp_c))  # q에 추가


N, M = map(int, input().split())
miro = [list(map(int, input())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
BFS(0, 0)
