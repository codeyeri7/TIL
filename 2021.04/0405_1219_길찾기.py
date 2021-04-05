def DFS(S):
    visited[S] = 1
    road.append(S)  # 지나간 길을 체크하기
    for i in range(100):
        if arr[S][i] == 1 and visited[i] == 0:
            DFS(i)  # 재귀


for T in range(1, 11):
    # 테스트케이스, 길의 개수
    tc, N = map(int, input().split())
    # 빈 행렬 만들기
    arr = [[0] * 100 for _ in range(100)]
    visited = [0] * (100)  # 방문체크용
    # 숫자 순서쌍 인풋
    num = list(map(int, input().split()))
    road = []  # 지나간 길
    # 순서쌍을 이용해 유향그래프 저장
    for i in range(len(num)):
        if i % 2 == 0:
            arr[num[i]][num[i+1]] = 1
    S = 0  # 출발지점
    G = 99  # 도착지점
    DFS(S)
    # 지나간 길(road)에 G가 있는지
    ans = 0
    for i in range(len(road)):
        if road[i] == G:
            ans = 1  # 있으면 1
            break
        else:
            ans = 0  # 없으면 0
    print("#{} {}".format(T, ans))
