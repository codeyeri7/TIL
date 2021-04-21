# 재귀로 해야할 것 같음
# 왜? - 경로에 이미 들어있으면 넘겨야 하는데 Q로 하니까 그게 어려운 듯
# 그래서 조건에 안 맞으면 재귀로 돌아가야하지 않을까...?

def BFS(r, c):
    global road
    Q = []
    Q.append((r, c))
    visited = [0] * N  # 방문체크
    visited[r] = 1  # 시작부터 체크하기
    road.append(r+1)  # 경로에 추가

    while Q:
        go_r, go_c = Q.pop(0)
        road.append(go_c+1)  # 무향이기 때문에 go_c에 갈 수 있는 정점이 있다
        visited[go_c] = 1  # 방문체크
        for i in range(N):
            # 인접 정점이 있고, 방문하지 않은 정점이라면
            if graph[go_c][i] == 1 and visited[i] == 0:
                Q.append((go_c, i))  # Q에 추가
    return road


for T in range(1, int(input())+1):
    N, M = map(int, input().split())
    graph = [[0] * N for _ in range(N)]
    for i in range(M):  # 간선수만큼 정점의 정보가 있으니
        arr = list(map(int, input().split()))
        graph[arr[0]-1][arr[1]-1] = 1
        graph[arr[1]-1][arr[0]-1] = 1
    result = []
    for j in range(N):
        for k in range(N):
            # 시작점찾기
            if graph[j][k] == 1:
                x = j
                y = k
                road = []
                BFS(x, y)
                result.append(len(road))
    if len(result) == 0:
        print("#{} {}".format(T, 1))
    else:
        print("#{} {}".format(T, max(result)))