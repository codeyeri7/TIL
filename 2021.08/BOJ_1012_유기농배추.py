d_r = [1, -1, 0, 0]
d_c = [0, 0, -1, 1]
def DFS(a, b):
    # 스택에 추가
    stack = [[a, b]]

    while stack:
        # 스택에 담겨있는 수 r, c로 지정
        r, c = stack[0][0], stack[0][1]
        del stack[0]  # 스택 제거
        for i in range(4):  # 4방향 탐색
            # 앞으로 가야할 위치(현재에서 4방향으로 가는 것)
            temp_r = r + d_r[i]
            temp_c = c + d_c[i]
            # 범위내일때만
            if 0 <= temp_r < N and 0 <= temp_c < M and baechu[temp_r][temp_c] == 1:
                baechu[temp_r][temp_c] = 0  # 방문체크
                # (근데 처음에 도착해서 0으로 체크하니까 안된다. 앞으로 가야할 곳을 체크해야 제대로 동작. 왜인지 모르겠음ㅠ)
                stack.append([temp_r, temp_c])  # 스택에 추가


tc = int(input())
for T in range(tc):
    M, N, K = map(int, input().split())
    baechu = [[0] * M for _ in range(N)]
    bug_cnt = 0
    bugs = []
    for i in range(K):
        a, b = map(int, input().split())
        baechu[b][a] = 1  # 배추 위치 체크
    for i in range(N):
        for j in range(M):
            if baechu[i][j] == 1:  # 배추가 있을 때에만
                DFS(i, j)  # DFS로 탐색
                bug_cnt += 1  # 벌레 카운트
    print(bug_cnt)
