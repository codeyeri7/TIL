# 시간초과 뜸...

import copy

# 조합
def combination(idx, sidx):
    if sidx == R:
        new_sel = []  # 이렇게 새로운 객체로 만드는 것으로 가능(sel이 같은 값만 저장될 때)
        for i in range(len(sel)):
            new_sel.append(sel[i])
        save.append(new_sel)
        return
    if idx == N:
        return

    sel[sidx] = location[idx]
    combination(idx + 1, sidx + 1)  # 뽑고가기
    combination(idx + 1, sidx)  # 안뽑고가기

# 시간초과나서 제출을 위해 일단 주석처리함.
# 자리바꾸기
# def jari_change(lists):
#     # 조합으로 뽑은 숫자로 자리 바꾸기
#     total = []
#     for i in range(len(lists)):
#         for j in range(len(save)):
#             copy_list = copy.deepcopy(lists)
#             copy_list[i][save[j][0]], copy_list[i][save[j][1]] = copy_list[i][save[j][1]], copy_list[i][save[j][0]]
#             total.append(copy_list[i][:])  # 슬라이싱으로도 가능(같은 값만 저장될 때 해결방법)
#     return total


for T in range(1, int(input())+1):
    num, change = input().split()
    # 숫자판의 인덱스를 이용해 자리를 바꾸기 위해 자리를 저장하는 location 생성
    arr = [list(num)]
    change = int(change)
    location = []
    for i in range(len(arr[0])):
        location.append(i)
    N = len(location)
    R = 2  # 숫자판 2개씩 뽑아서 자리 교체

    sel = [0] * R
    save = []

    combination(0, 0)
    # print(save)
    cnt = 0
    while cnt < change:
        jari_change(arr)
        ans = jari_change(arr)
        arr = ans
        cnt += 1

    a = []
    for i in arr:
        result = int(''.join(i))
        a.append(result)
    # print(max(a))
    print("#{} {}".format(T, max(a)))
