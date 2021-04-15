def perm(idx):
    global every_sel
    if idx == num_cnt:
        every_sel.append()
        print(sel)
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
    work = []
    home = []
    work.append(info.pop(0))
    work.append(info.pop(0))
    home.append(info.pop(0))
    home.append(info.pop(0))
    good_road = 0
    n = 0
    num = []
    for i in range(0, len(info), 2):
        num.append(i)
    num_cnt = len(num)

    sel = [0] * num_cnt  # 결과들이 저장될 리스트
    check = [0] * num_cnt  # 해당 원소를 이미 사용했는지 안했는지에 대한 체크
    every_sel = []

    perm(0)


    # while len(info) > 2:
    #     a = info.pop(n)
    #     b = info.pop(n)
    #     min_road = 200
    #     min_idx = 0
    #     for i in range(0, len(info), 2):
    #         x = abs(a - info[i])
    #         y = abs(b - info[i + 1])
    #         if x + y < min_road:
    #             min_road = x + y
    #             min_idx = i
    #     good_road += min_road
    #     n = min_idx
    #
    # good_road += abs(home[0] - info[0]) + abs(home[1] - info[1])
    # print("#{} {}".format(T, good_road))

    # print(work)
    # print(home)
    # print(info)
    # print(num)
    # print(num_cnt)
    # print(sel)
    # print(check)
    print(every_sel)


# 이렇게 하는게 아니라 회사랑 집 빼고
# 가야하는 손님들의 집을 순열로 갈 수 있는 경로를 다 만들어서
# 그 경로대로 갔을 떄를 구한 후
# 그 경로들 중 최적의 경로를 찾아야 함
# 다시 풀기(순열조합으로)
