def Dijkstra(s, A, D):
    U[s] = 1
    cnt = 0
    for v in range(N+1):
        D[v] = A[s][v]
    while cnt < N+1:
        min_num = 987654321
        min_idx = 0
        # D에서 최소값 찾기
        for i in range(N+1):
            if i != s:
                # 방문한 적 없으면서 D[i]의 최소값보다 작으면
                # 최소값 설정
                if U[i] == 0 and D[i] <= min_num:
                    min_num = D[i]
                    min_idx = i
        for j in range(N+1):
            # 방문한 적 없으면서 최소값이면 방문체크 후
            if U[j] == 0 and min_idx == j:
                U[j] = 1
                for k in range(N+1):
                    D_min = []
                    # 최소값 갱신하기
                    if 0 < A[j][k] and A[j][k] < 100:
                        D_min.append(D[k])
                        D_min.append(D[j]+A[j][k])
                        D[k] = min(D_min)
        cnt += 1


for T in range(1, int(input())+1):
    N, E = map(int, input().split())
    # 무한대말고 100으로 설정(구간거리가 최대 10이니까)
    A = [[100 for _ in range(N+1)] for _ in range(N+1)]
    # 인접리스트 만들기
    for i in range(E):
        node_info = list(map(int, input().split()))
        A[node_info[0]][node_info[1]] = node_info[2]
    # 0,0 / 1,1 이런 위치도 0으로 설정
    for i in range(N+1):
        A[i][i] = 0
    D = [0] * (N+1)  # 거리
    U = [0] * (N+1)  # 선택된 정점 집합
    Dijkstra(0, A, D)
    print("#{} {}".format(T, D[N]))