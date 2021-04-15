def perm(idx):  # 순열
    if idx == area:
        # 새로운 객체를 만들어 거기에 넣어줘서 sel의 마지막값이 반복되어 들어가지 않도록 방지
        new_sel = []
        for i in range(len(sel)):
            new_sel.append(sel[i])
        save.append(new_sel)
        return
    else:
        for i in range(area):
            if check[i] == 0:
                sel[idx] = arr[i]  # 셀에 값 입력
                check[i] = 1  # 사용을 했다는 표시
                perm(idx+1)  # 재귀
                check[i] = 0  # 다시 원상복귀

for T in range(1, int(input())+1):
    N = int(input())
    # 배터리 사용량 인풋
    battery = [list(map(int, input().split())) for _ in range(N)]

    # 경로 찾기위해 순열 찾기
    # 0 : 사무실, 1~N-1 까지의 순열을 찾아야 함
    arr = []  # 가야하는 구역 : 1부터 N
    for i in range(1, N):
        arr.append(i)

    area = len(arr)
    sel = [0] * area  # 결과가 저장되는 리스트
    check = [0] * area  # 해당 원소를 이미 사용했는지 체크
    save = []

    perm(0)
    b_total = []

    for i in range(len(save)):
        b_cnt = 0  # 배터리 소모량
        # 사무실에서 첫번째 구역
        b_cnt += battery[0][save[i][0]]
        for j in range(1, len(save[i])):
            # 구역에서 구역끼리의 이동
            b_cnt += battery[save[i][j-1]][save[i][j]]
        # 마지막 구역에서 사무실로 복귀
        b_cnt += battery[save[i][-1]][0]
        # 모든 배터리 사용량 경우의 수를 저장
        b_total.append(b_cnt)
    print("#{} {}".format(T, min(b_total)))