# 조건 : 양쪽구간을 번갈아 선택하는 숫자
# --> 한번에 찾아도 조건 성립..
# --> 왼쪽 - 오른쪽 - mid == key이면 OK
# --> 왼쪽 - mid == key여도 OK
# 그럼 조건 성립 안 되는건 뭐야?
# --> 연속으로 오른쪽으로 가거나 연속으로 왼쪽으로 + 아예 없을 때


def binary_search(mlist, low, high, key):
    global result
    if low > high:  # key값이 mlist에 없는 경우
        result.append(3)
        return
    else:
        mid = (low+high) // 2  # 중간 값
        # key값을 mid에서 찾음
        if key == mlist[mid]:
            result.append(2)
            return mid
        # 왼쪽 구간에서 찾기
        elif key < mlist[mid]:
            result.append(1)
            return binary_search(mlist, low, mid-1, key)
        # 오른쪽 구간에서 찾기
        else:
            result.append(0)
            return binary_search(mlist, mid+1, high, key)


for T in range(1, int(input())+1):
    N, M = map(int, input().split())
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))
    A_list = sorted(A_list)
    cnt = 0
    for i in range(M):
        n = B_list[i]
        result = []
        binary_search(A_list, 0, N-1, n)
        correct = 1
        # result에서 연속된 숫자가 나오면 조건에 성립 X
        # 3이 나오면 그 숫자는 A_list에 없었다는 거니까 조건에 성립 X
        for j in range(1, len(result)):
            if result[j] == result[j-1]:
                correct = 0
            elif result[j] == 3:
                correct = 0
        cnt += correct
    print("#{} {}".format(T, cnt))