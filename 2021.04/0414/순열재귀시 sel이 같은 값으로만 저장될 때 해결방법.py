# import copy

arr = [1, 2, 3]

N = len(arr)

sel = [0] * N #결과들이 저장될 리스트
check = [0] *N #해당 원소를 이미 사용했는지 안했는지에 대한 체크
save = []

def perm(idx):
    #다 뽑아서 정리했다면
    if idx == N:
        # 그냥 sel을 더하면 맨 마지막 sel 값이 계속 더해짐. 슬라이싱을 이용해 전체범위를 슬라이싱해서 새로 배열을 파는 것.
        # save.append(sel[:])
        # 딥카피도 가능하다
        # nums = copy.deepcopy(sel)
        # save.append(nums)
        new_sel = []  # 이렇게 새로운 객체로 만드는 것도 가능
        for j in range(len(sel)):
            new_sel.append(sel[j])
        save.append(new_sel)
        return
    else:
        for i in range(N):
            if check[i] == 0:
                sel[idx] = arr[i] #값을 써라
                check[i] = 1 #사용을 했다는 표시
                perm(idx+1)
                check[i] = 0 #다음 반복문을 위한 원상복구


perm(0)
print(save)

