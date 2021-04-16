for T in range(1, int(input())+1):
    N = int(input())
    # 방 인풋
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0] * (N*N+1)  # 주변에 +1번의 방이 있는지를 알기 위한 배열 만들기
    for i in range(N):
        for j in range(N):
            # 사방탐색(상하좌우)
            for k in range(4):
                dr = [-1, 1, 0, 0]
                dc = [0, 0, 1, -1]
                r = i + dr[k]
                c = j + dc[k]
                # 범위 내에 없으면 다시 탐색
                if r < 0 or r >= N or c < 0 or c >= N:
                    continue
                # 현재 위치에서 +1인 방이 있으면
                if arr[r][c] == arr[i][j] + 1:
                    # 배열 v의 방 번호 자리에 1
                    v[arr[i][j]] = 1
    cnt = 0  # 1의 개수 카운트
    max_cnt = 0  # 그 중 연속된 방이 많을 때 카운트 저장
    idx = N*N  # max_cnt의 인덱스
    # 배열 뒤에서 부터 출발(연속된 방의 개수가 같은 때 가장 작은 번호가 출력이라서 가장 왼쪽 idx가 나와야 함)
    for i in range(len(v)-1, -1, -1):
        # 배열의 가장 끝의 방에서 i+1을 하면 인덱스 에러가 나니까
        # 가장 끝 방의 앞부터 i+1가 0인 경우 찾기
        if i < len(v)-1 and v[i+1] == 0:
            cnt = 0  # cnt 초기화
        # 배열에서 1을 찾으면 cnt +1
        if v[i] == 1:
            cnt += 1
        # 1이 없으면 연속된 방의 개수 세기 끝.
        elif v[i] == 0:
            # max_cnt를 찾아 저장하고, 그 idx를 찾는다.
            # 지금 위치는 1이 연속으로 있다가 이제 없는 경우니까
            # idx는 i+1을 해줘야 함.
            if cnt >= max_cnt:
                max_cnt = cnt
                idx = i+1
    print("#{} {} {}".format(T, idx, max_cnt+1))