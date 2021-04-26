# 테케 10개 중 9개 맞음.... 원인을 모르겠습니다....ㅠ
def prim(s, A, D):
    U[s] = 1  # 방문체크
    for i in range(V+1):  # D에 시작점에서 인접한 가중치 넣어주기
        D[i] = A[s][i]
    cnt = 0
    while cnt < V+1:  # cnt가 정점의 개수와 같으면 멈추도록! 근데 <= 이어도 결과는 같다 밑에서 return해줘서 그런가?
        min_num = 987654321
        min_idx = 1001
        for j in range(V+1):
            # 0보다 크고 100보다 작으면서 방문하지 않은 경우에만
            if 0 < A[s][j] and A[s][j] < 100 and U[j] == 0:
                if min_num >= A[s][j]:  # 최소값 찾기
                    min_num = A[s][j]
                    min_idx = j
                # D에 저장된 가중치보다 작으면 갱신
                if D[j] > A[s][j]:
                    D[j] = A[s][j]
        if min_idx == 1001:  # 최소값이 갱신 안 된 경우는 끝낸기
            return
        else:  # 최소값 갱신됐으면 출발점 바꾸고, U에 방문체크
            s = min_idx
            U[min_idx] = 1
            cnt += 1


for T in range(1, int(input())+1):
    V, E = map(int, input().split())
    A = [[100] * (V+1) for _ in range(V+1)]
    for i in range(E):  # 인접행렬만들기
        node_info = list(map(int, input().split()))
        A[node_info[0]][node_info[1]] = node_info[2]
        A[node_info[1]][node_info[0]] = node_info[2]
    for i in range(V+1):
        A[i][i] = 0
    U = [0] * (V+1)  # 방문체크
    D = [0] * (V+1)  # 가중치
    prim(0, A, D)
    print("#{} {}".format(T, sum(D)))