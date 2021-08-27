from collections import deque


def DFS(v):
    # 방문체크
    visit_dfs[v] = 1
    print(v, end=" ")  # 출력
    for j in range(1, N + 1):
        # v의 인접 정점 중 방문 안 한 것 찾기
        if visit_dfs[j] == 0 and arr[v][j] == 1:
            DFS(j)  # 찾으면 재귀


def BFS(v):
    q = deque()
    # q에 출발한 정점 넣기
    q.append(v)
    # 방문체크
    visit_bfs[v] = 1
    while q:  # q가 비어있지 않은 동안 계속 반복
        v = q.popleft()  # 맨 위에 있는 거 꺼내서
        print(v, end=" ")  # 출력
        for j in range(1, N + 1):
            # 방문 안 했고, 가야 할 정점 찾기
            if visit_bfs[j] == 0 and arr[v][j] == 1:
                q.append(j)  # q에 추가
                visit_bfs[j] = 1  # 방문체크

N, M, V = map(int, input().split())
# 배열 만들기
arr = [[0] * (N + 1) for _ in range(N + 1)]
# 방문체크 만들어주기
visit_dfs = [0] * (N + 1)
visit_bfs = [0] * (N + 1)
# 인접 정점을 알기 위해
for i in range(M):
    a, b = map(int, input().split())
    arr[a][b] = arr[b][a] = 1

DFS(V)
print()
BFS(V)