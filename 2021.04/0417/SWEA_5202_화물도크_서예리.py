for T in range(1, int(input())+1):
    N = int(input())  # 작업 횟수
    for i in range(N):
        # 화물 싣는 작업 시간
        hwamul = [list(map(int, input().split())) for _ in range(N)]
        hwamul.sort(key=lambda x: x[1])  # 람다로 종료 시간이 빠른 순으로 정렬
        cnt = 0
        finish = 0  # 이전 작업이 끝나는 시간
        for j in range(N):
            # 만약 이전 작업이 끝난 시간보다 지금 작업 시작 시간이 앞이면
            if finish <= hwamul[j][0]:
                cnt += 1  # 카운트 추가
                # 작업 끝나는 시간 갱신
                finish = hwamul[j][1]
        print(cnt)
