def Dijkstra(s, A, D):
    U[s] = 1
    cnt = 0
    for v in range(N):
        D[v] = A[s][v]
    while cnt < N:
        min_num = 987654321
        min_idx = 0
        # D에서 최소값 찾기
        for i in range(N):
            if i != s:
                if U[i] == 0 and D[i] <= min_num:
                    min_num = D[i]
                    min_idx = i
        for j in range(N):
            if U[j] == 0 and min_idx == j:
                U[j] = 1
                for k in range(N):
                    D_min = []
                    if 0 < A[j][k] and A[j][k] < 100:
                        D_min.append(D[k])
                        D_min.append(D[j]+A[j][k])
                        D[k] = min(D_min)
        cnt += 1

N = 6
A = [[0, 3, 4, 100, 100, 100], [100, 0, 100, 5, 100, 100], [100, 1, 0, 4, 5, 100], [100, 100, 100, 0, 3, 4], [3, 100, 100, 100, 0, 5], [100, 100, 100, 100, 100, 0]]
# A = [[100 for _ in range(N)] for _ in range(N)]
# 0 0 1 3 2 4
# 1 0 3 5
# 1 1 2 0 3 4 4 5
# 3 0 4 3 5 4
# 0 3 4 0 5 5
# 5 0
# for i in range(N):
#     arr = list(map(int, input().split()))
#     for j in range(len(arr)):
#         if j % 2 == 0:
#             A[i][arr[j]] = arr[j+1]
D = [0] * N  # 거리
U = [0] * N  # 선택된 정점 집합
Dijkstra(0, A, D)
print(D)