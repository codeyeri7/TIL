def DFS(v):
    global cnt
    visited[v] = 1  # 방문체크
    for j in range(1, N+1):
        # 아직 바이러스에 걸리지 않으면서 인접한 컴퓨터일 때만
        if visited[j] == 0 and arr[v][j] == 1:
            cnt += 1  # 새로 바이러스에 걸리는 컴퓨터를 찾았을 때만 cnt하기
            DFS(j)
    return cnt


N = int(input())
M = int(input())
arr = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 0

# 인접 컴퓨터 행렬로 찾아놓기
for i in range(M):
    a, b = map(int, input().split())
    arr[a][b] = arr[b][a] = 1

# 출발지점이 1이니까 
ans = DFS(1)
print(ans)

