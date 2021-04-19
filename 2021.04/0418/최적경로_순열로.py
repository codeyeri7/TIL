def perm(idx):  # 순열
    global every_sel
    if idx == num_cnt:
        every_sel.append(sel[::-1])
        return
    else:
        for i in range(num_cnt):
            if check[i] == 0:
                sel[idx] = num[i]  # 값을 써라
                check[i] = 1  # 사용을 했다는 표시
                perm(idx + 1)
                check[i] = 0  # 다음 반복문을 위한 원상복구


for T in range(1, int(input()) + 1):
    N = int(input())
    info = list(map(int, input().split()))
    work = []  # 회사
    home = []  # 집
    work.append(info.pop(0))
    work.append(info.pop(0))
    home.append(info.pop(0))
    home.append(info.pop(0))
    num = []
    for i in range(0, len(info), 2):
        num.append(i)
    num_cnt = len(num)
    # print(info)
    sel = [0] * num_cnt  # 결과들이 저장될 리스트
    check = [0] * num_cnt  # 해당 원소를 이미 사용했는지 안했는지에 대한 체크
    every_sel = []
    perm(0)
    min_road = 2000
    # i = 0
    for i in range(len(every_sel)):
        result = False
        road = 0
        # 회사에서 첫번째 손님 집의 거
        road += abs(work[0] - info[every_sel[i][0]]) + abs(work[1] - info[every_sel[i][0] + 1])
        for j in range(N - 1):
            p = every_sel[i][j]
            a = info[p]  # 손님 집 x축
            b = info[p + 1]  # 손님 집 y축
            n = every_sel[i][j + 1]  # 다음 손님 집 인덱스
            road += abs(a - info[n]) + abs(b - info[n + 1])
            if road > min_road:
                result = True
                continue
        if result == True:
            continue
        # 마지막 손님 집에서 직원 집으로
        road += abs(info[every_sel[i][N - 1]] - home[0]) + abs(info[every_sel[i][N - 1] + 1] - home[1])
        if road <= min_road:  # 그 중 최단거리 저장
            min_road = road
    print("#{} {}".format(T, min_road))