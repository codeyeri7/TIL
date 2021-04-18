for T in range(1, int(input()) + 1):
    N = int(input())
    info = list(map(int, input().split()))
    work = []  # 회사
    home = []  # 집
    work.append(info.pop(0))
    work.append(info.pop(0))
    home.append(info.pop(0))
    home.append(info.pop(0))

    good_road = 0  # 최종 최적 경로
    min_road = 200
    min_idx = 0
    # 회사에서 첫번째 손님 집
    for i in range(0, len(info), 2):
        road = abs(work[0] - info[i]) + abs(work[1] - info[i + 1])
        if road <= min_road:
            min_road = road
            min_idx = i
    good_road += min_road
    a = info.pop(min_idx)
    b = info.pop(min_idx)
    # 손님 집 중 직원 집과 가장 가까운 곳 구하기
    min_road = 200
    min_idx = 0
    for i in range(0, len(info), 2):
        road = abs(info[i] - home[0]) + abs(info[i+1] - home[1])
        if road <= min_road:
            min_road = road
            min_idx = i
    good_road += min_road
    last_a = info.pop(min_idx)
    last_b = info.pop(min_idx)
    # 손님들의 집
    while len(info) > 0:
        min_road = 200
        min_idx = 0
        for j in range(0, len(info), 2):
            road = abs(a - info[j]) + abs(b - info[j+1])
            if road <= min_road:
                min_road = road
                min_idx = j
        good_road += min_road
        a = info.pop(min_idx)
        b = info.pop(min_idx)
    # 손님들 집 돌고 마지막 손님집 가기
    # road = abs(a - last_a) + abs(b - last_b)
    # good_road += road
    print(good_road)
